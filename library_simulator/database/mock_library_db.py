from library_simulator.queues.list_queue import ListQueue

class MockLibraryDb:
    """
    Represents an in-memory mock database for use in simulation.
    Stores all relevant library state: books, cardholders, return queue, and reserved holds.
    """

    def __init__(self, book_catalogue, cardholder_dict):
        """
        Initializes the mock database with pre-seeded books and cardholders.

        Args:
            book_catalogue (dict): A dictionary mapping ISBNs to Book objects.
            cardholder_dict (dict): A dictionary mapping card numbers to Cardholder objects.
        """
        self.book_catalogue = book_catalogue
        self.cardholder_dict = cardholder_dict
        self.returns_queue = ListQueue()
        self.reserved_holds = {} # Key: card_number, Value: List[Hold]

    def lookup_book(self, isbn):
        """
        Retrieves a book from the catalogue by its ISBN.

        Args:
            isbn (str): The ISBN of the book to look up.

        Returns:
            Book: The matching Book object.

        Raises:
            KeyError: If the ISBN does not exist in the catalogue.
        """
        # TODO:
        #  if not found: handle error
        return self.book_catalogue[isbn]

    def lookup_cardholder(self, card_number):
        return self.cardholder_dict[card_number]
