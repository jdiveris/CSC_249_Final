from library_simulator.queues.list_queue import ListQueue

class MockLibraryDb:
    """
    Represents an in-memory mock database for use in simulation.
    Stores all relevant library state: books, library_cards, return queue, and reserved holds.
    """

    def __init__(self, book_catalogue, library_card_dict):
        """
        Initializes the mock database with pre-seeded books and library_cards.

        Args:
            book_catalogue (dict): A dictionary mapping ISBNs to Book objects.
            library_card_dict (dict): A dictionary mapping card numbers to LibraryCard objects.
        """
        self.book_catalogue = book_catalogue
        self.library_card_dict = library_card_dict
        self.returns_queue = ListQueue()
        self.reserved_holds = {} # Key: card_number, Value: List[Hold]
        self.active_cards = set() # Used to increment loan hold/timers

    def lookup_book(self, isbn):
        """
        Retrieves a book from the catalogue by its ISBN.

        Args:
            isbn (str): The ISBN of the book to look up.

        Returns:
            Book: The matching Book object.
        """
        return self.book_catalogue[isbn]

    def lookup_library_card(self, card_number):
        return self.library_card_dict[card_number]
