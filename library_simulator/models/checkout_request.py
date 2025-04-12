class CheckoutRequest:
    """
    Represents a checkout job initiated by a library_card.
    Each request includes a list of books to check out and tracks how many remain to be processed.
    """

    def __init__(self, library_card, book_list):
        """
        Initializes a new checkout request.

        Args:
            library_card (LibraryCard): The user attempting to check out books.
            book_list (List[Book]): A list of Book objects to be checked out.
        """
        self.library_card = library_card
        self.book_list = book_list
        # Set a size attribute equal to the length of book_list
        self.remaining_books = len(book_list)

    def is_complete(self):
        """
        Checks whether all books in the request have been scanned.

        Returns:
            bool: True if all books have been processed; False otherwise.
        """
        return self.remaining_books <= 0

    def scan_book(self):
        """
        Processes (scans) the next book in the checkout queue.

        Returns:
            Book: The next Book object to be checked out.

        Raises:
            IndexError: If called when there are no books left to scan.
        """
        # If there are no more books remaining, raise error
        if self.remaining_books <= 0:
            raise IndexError("There are no more books to scan")

        # Retrieve a book from the book list (removing it)
        book_scanned = self.book_list.pop()
        # Update remaining book quantity
        self.remaining_books = len(self.book_list)

        # Return the retrieved book
        return book_scanned
