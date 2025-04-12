from library_simulator.models.loan import Loan
from library_simulator.models.hold import Hold


class LibraryController:
    """
    Coordinates core library operations such as checking out books, placing holds,
    processing returns, and updating availability and hold queues.
    """

    def checkout_book(self, library_card, book):
        """
        Attempts to check out a book for the given library_card.
        If the book is available, it is loaned and recorded in the library_card's loan queue.
        If unavailable, a hold is placed on the book instead.

        Args:
            library_card (LibraryCard): The user attempting to check out a book.
            book (Book): The book being requested.
        """
        if book.is_available():
            # If book is available, reduce available quantity and create a loan
            # Add that loan to the library_card's loan_queue
            book.available_copies -= 1
            library_card.loan_queue.enqueue(Loan(library_card.card_number, book.isbn))
        else:
            # If book is not available place a hold for this library_card
            self.place_hold(book, library_card)

    def pickup_book(self, hold, mock_database):
        """
        Checks out a book from a hold.
        Looks up the book object from the isbn in the hold, makes a copy
        available for pickup, then checks it out using the card number from hold.

        Args:
            hold (Hold): The hold for the book to be picked up.
            mock_database (MockLibraryDB): The mocked database containing book and
                library_card info.

        """
        # Get book that hold is referring to via hold info
        book = mock_database.lookup_book(hold.isbn)
        # Increase available copies of the book (so one can be checked out)
        book.available_copies += 1

        # Checkout book (Lookup library_card via hold info)
        self.checkout_book(mock_database.lookup_library_card(hold.card_number), book)
        self.hold_checked_out(hold, mock_database.reserved_holds)

    def place_hold(self, book, library_card):
        """
        Places a hold on a book for a specific library_card.

        Args:
            book (Book): The book to place a hold on.
            library_card (LibraryCard): The user placing the hold.
        """
        # Create a hold obj and enqueue it in the book's hold_queue
        book.hold_queue.enque(Hold(book.isbn, library_card.card_number))

    def hold_checked_out(self, hold, reserved_holds):
        """
        Removes a hold from the reserved holds collection after it has been checked out.
        If the cardholder has no remaining holds, their entry is removed from the dictionary.

        Args:
            hold (Hold): The hold object that was picked up.
            reserved_holds (dict): A dictionary mapping card numbers to lists of Hold objects.
        """
        # Remove hold from reserved list
        reserved_holds[hold.card_number].remove(hold)
        # If there are no more reserved holds, remove the card number from reserved_holds
        if not reserved_holds[hold.card_number]:
            del reserved_holds[hold.card_number]

    def remove_hold(self, hold, mock_database):
        """
        Removes a hold from both the book's hold queue and the cardholder's reserved holds list.

        Args:
            hold (Hold): The hold object to be removed.
            mock_database (MockLibraryDb): The mock database containing book and hold records.
        """
        # Lookup the book associated with the hold
        book = mock_database.lookup_book(hold.isbn)
        # Remove the hold from the book's hold queue
        book.hold_queue.remove(hold)
        # Remove the hold from the reserved_holds list
        mock_database.reserved_holds[hold.card_number].remove(hold)

    def return_book(self, library_card, mock_database):
        """
        Initiates a book return by dequeuing the next book from the library_card's loan queue
        and adding it to the library's return queue.

        Args:
            library_card (LibraryCard): The user returning a book.
            mock_database (MockLibraryDb): The mock database containing the return queue.
        """
        # Fetch the oldest book checked out by library_card
        book = library_card.loan_queue.dequeue()
        # Add the book to the library's return_queue
        mock_database.return_queue.enque(book)

    def process_return(self, mock_database):
        """
        Processes the next book in the return queue.
        If the returned book has pending holds, assigns the book to the next hold in line.

        Args:
            mock_database (MockLibraryDb): The mock database containing books and queues.
        """
        # Fetch the oldest return
        book = mock_database.return_queue.dequeue()

        if book.has_holds():
            # Access the first hold on this book without removing
            first_hold = book.hold_queue.peek()
            # Set time to claim hold to 1 week
            first_hold.time_to_claim = 7
            # Mark hold as available
            first_hold.available = True
            # Get card number associated with hold
            card_number = first_hold.card_number
            # Add hold to reserved books list in database
            if card_number not in mock_database.reserved_holds:
                mock_database.reserved_holds[card_number] = [first_hold,]
            else:
                mock_database.reserved_holds[card_number].append(first_hold)
        else: # If book has no holds
            # Increase the available copies for rental
            book.available_copies += 1


    def check_for_available_holds(self):
        pass