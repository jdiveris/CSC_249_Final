import random

from controller.library_controller import LibraryController
from database.mock_library_db import MockLibraryDb
from queues.list_queue import ListQueue
from seed_data.seeder import seed_books, seed_library_cards
from utils.clock import Clock
from utils.log_report import LogReport
from models.checkout_request import CheckoutRequest
from models.pickup_request import PickupRequest


class Simulator:
    """
    Manages the progression of simulated library activity over a series of time-based ticks.
    Orchestrates library_card arrivals, checkout jobs, pickup requests, and return processing.
    """

    def __init__(self):
        """
        Initializes the simulation environment, seeding data and setting up time and queues.
        """
        self.db = MockLibraryDb(seed_books(), seed_library_cards())
        self.librarian = LibraryController()
        self.clock = Clock(hours_per_day=12)
        self.logger = LogReport()
        self.checkout_queue = ListQueue()
        self.working_request = None

    def run(self, days=30):
        """
        Runs the main simulation loop over the specified number of simulated days.
        At each hour (tick), new patrons may arrive, requests may be processed,
        and returns may be handled when the system is idle.

        Args:
            days (int): The number of simulated days to run. Default is 30.
        """
        # Simulation will loop each hour and each day
        self.logger.log_event("=== SIMULATION START ===\n"
                              "===============================\n")
        for _ in range(days):  # Loop for days
            self.logger.log_event("Day started")
            for _ in range(self.clock.hours_per_day):  # Loop for hours
                # Increase the hours on the clock
                self.clock.tick()

                # Generate random patron arrivals at the library
                self.generate_random_num_of_arrivals()

                if self.working_request:
                    # If there is a current working_request, process it
                    self.process_working_request()
                elif self.checkout_queue.is_empty() \
                        and not self.db.returns_queue.is_empty():
                    # If no patron is in line to check out, and there are pending returns,
                    # process a return
                    self.librarian.process_return(self.db)
                elif not self.checkout_queue.is_empty():
                    # If there is a Request in the queue,
                    # assign it to the current working_request
                    self.working_request = self.checkout_queue.dequeue()

                    # Process the current working_request
                    self.process_working_request()

            # Loop through the days active cards
            for card in list(self.db.active_cards):
                # Loop through the active loans on those cards
                for loan in card.loan_queue:
                    # Decrement the loan periods by 1 day
                    loan.decrement_loan_period()
                    # If loan period is over, return book
                    if loan.is_elapsed():
                        # Return book and save book title
                        book_title = self.librarian.return_book(card, self.db)
                        # Log return
                        self.logger.log_return(card.card_number, book_title)

                # If card has reserved holds
                if card.card_number in self.db.reserved_holds:
                    # Loop through holds
                    for hold in self.db.reserved_holds[card.card_number]:
                        # Decrement hold time
                        hold.decrement_time_to_claim()
                        # If hold is expired, remove hold
                        if hold.has_expired():
                            self.librarian.remove_hold(hold, self.db)
                            # Log hold expiration
                            self.logger.log_event(
                                f"Hold for {card.card_number} on book \"{self.db.lookup_book(hold.isbn).title}\" expired and was removed"
                            )

                # Remove card from active cards if it has no loans or reserved holds
                if card.loan_queue.is_empty() and \
                        card.card_number not in self.db.reserved_holds:
                    self.db.active_cards.remove(card)

            # Log days events
            self.logger.log_event("Day ended")
            self.logger.log_day_summary(self.clock.current_day)

        # Generate end of simulation report
        self.logger.log_end_of_simulation()

    def process_working_request(self):
        """
        Processes the current active request, whether it's a checkout or a pickup.
        If the request is completed or fails, it clears the working slot.
        """
        # Catch if a completed working request was passed in error
        if self.working_request.is_complete():
            self.logger.log_event("Working request completed")
            # If completed, cloar working request and end process
            self.working_request = None
            return
        # If working request is a checkout
        if isinstance(self.working_request, CheckoutRequest):
            # Get first book to check out
            book = self.working_request.scan_book()
            # Attempt to check out book and save attempt status (CHECKOUT or HOLD)
            status = self.librarian.checkout_book(self.working_request.library_card, book)

            if status == "CHECKOUT":
                # Log successful checkout
                self.logger.log_checkout(self.working_request.library_card.card_number, book.title)
            elif status == "HOLD":
                # Log that a hold was placed instead
                self.logger.log_hold(self.working_request.library_card.card_number, book.title)
        # If working request is a hold pickup
        elif isinstance(self.working_request, PickupRequest):
            # Get first hold for pickup
            hold = self.working_request.fetch_hold()
            # Catch scenario where the working request is holdover from previous day
            # and hold has expired overnight
            if hold.has_expired():
                # Log expiration event
                self.logger.log_event(f"Hold on \"{self.db.lookup_book(hold.isbn).title}\" expired overnight")
            else:
                # Pickup the hold
                self.librarian.pickup_book(hold, self.db)
                # Log pickup event
                self.logger.log_pickup(self.working_request.library_card.card_number,
                                       self.db.lookup_book(hold.isbn).title)
        # Check if working request is now completed
        if self.working_request.is_complete():
            # Log completion of request
            self.logger.log_event("Working request completed")
            # Clear working request
            self.working_request = None

    def generate_random_num_of_arrivals(self):
        """
        Randomly determines how many patrons arrive during the current tick,
        with up to three attempts and a 25% chance per attempt.
        """
        # Initialize number of potential arrivals to 0
        n = 0
        # Loop minimum of 0 times, and a maximum of 3
        for _ in range(random.randint(0, 3)):
            # For each loop, a 25% chance to generate an arrival
            # (Maximum possible 3)
            if random.random() < .25:
                # Increase the number of arrivals
                n += 1
        if n > 0:
            # If at least arrival has been generated,
            # simulate that many patrons arriving
            self.simulate_arrivals(n)

    def simulate_arrivals(self, n):
        """
        Simulates the arrival of n patrons, creating either a checkout request
        or a pickup request based on whether the library_card has available holds.

        Args:
            n (int): The number of patrons arriving this tick.
        """
        # Get a random list of unique library_card objects from the database
        patrons = random.sample(list(self.db.library_card_dict.values()), n)

        # Loop through list of patrons
        for patron in patrons:
            # Log arrival time
            self.logger.log_event(f"{patron.card_number} arrived at hour {self.clock.current_hour}")
            # Track that patron's card is active
            self.db.active_cards.add(patron)
            # If patron has reserved holds available for pickup
            if patron.card_number in self.db.reserved_holds and \
                    len(self.db.reserved_holds[patron.card_number]) > 0:
                # Get list of holds
                holds_to_pickup = [
                    hold for hold in self.db.reserved_holds.get(patron.card_number, [])
                    if not hold.fulfilled and not hold.has_expired()
                ]
                if holds_to_pickup:
                    self.checkout_queue.enqueue(PickupRequest(patron, holds_to_pickup))
            else:
                # Generate a random number of books for patron to attempt to borrow
                num_of_books = random.randint(1, 3)
                # Get a random list of unique book objects from the database
                books = random.sample(list(self.db.book_catalogue.values()), num_of_books)
                # Create a CheckoutRequest for the patron and the book list
                checkout_request = CheckoutRequest(patron, books)

                # Add the CheckoutRequest to the checkout_queue
                self.checkout_queue.enqueue(checkout_request)
