from library_simulator.models.loan import Loan
from library_simulator.models.hold import Hold


class LibraryController:
    """
    Coordinates core library operations such as checking out books, placing holds,
    processing returns, and updating availability and hold queues.
    """

    def checkout_book(self, cardholder, book):
        """
        Attempts to check out a book for the given cardholder.
        If the book is available, it is loaned and recorded in the cardholder's loan queue.
        If unavailable, a hold is placed on the book instead.

        Args:
            cardholder (Cardholder): The user attempting to check out a book.
            book (Book): The book being requested.
        """
        if book.is_available():
            # If book is available, reduce available quantity and create a loan
            # Add that loan to the cardholder's loan_queue
            book.available_copies -= 1
            cardholder.loan_queue.enqueue(Loan(cardholder.card_number, book.isbn))
        else:
            # If book is not available place a hold for this cardholder
            self.place_hold(book, cardholder)

    def pickup_book(self, hold, mock_database):
        # Get book that hold is referring to via hold info
        book = mock_database.lookup_book(hold.isbn)
        # Increase available copies of the book (so one can be checked out)
        book.available_copies += 1

        # Checkout book (Lookup cardholder via hold info)
        self.checkout_book(mock_database.lookup_cardholder(hold.card_number), book)

    def place_hold(self, book, cardholder):
        """
        Places a hold on a book for a specific cardholder.

        Args:
            book (Book): The book to place a hold on.
            cardholder (Cardholder): The user placing the hold.
        """
        # Create a hold obj and enqueue it in the book's hold_queue
        book.hold_queue.enque(Hold(book.isbn, cardholder.card_number))

    def return_book(self, cardholder, mock_database):
        """
        Initiates a book return by dequeuing the next book from the cardholder's loan queue
        and adding it to the library's return queue.

        Args:
            cardholder (Cardholder): The user returning a book.
            mock_database (MockLibraryDb): The mock database containing the return queue.
        """
        # Fetch the oldest book checked out by cardholder
        book = cardholder.loan_queue.dequeue()
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
            if card_number not in mock_database.reserved_books:
                mock_database.reserved_books[card_number] = [first_hold,]
            else:
                mock_database.reserved_books[card_number].append(first_hold)
        else: # If book has no holds
            # Increase the available copies for rental
            book.available_copies += 1


    def check_for_available_holds(self):
        pass