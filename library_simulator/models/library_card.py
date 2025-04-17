from library_simulator.queues.list_queue import ListQueue

class LibraryCard:
    """
    Represents a library card issued to a patron.

    Attributes:
        card_number (str): Unique identifier for the library card.
        loan_queue (ListQueue): Queue of books currently loaned out under this card.
    """

    def __init__(self, card_number):
        """
        Initializes a new LibraryCard instance.

        Args:
            card_number (str): The unique ID of the library card.
        """
        self.card_number = card_number
        self.loan_queue = ListQueue()

    def __repr__(self):
        """
        Returns a string representation for debugging.

        Returns:
            str: Debug-style string with card number and number of active loans.
        """
        return f"<LibraryCard #{self.card_number}, loans={len(self.loan_queue)}>"

    def __str__(self):
        """
        Returns a readable string for display purposes.

        Returns:
            str: Friendly description of the library card and active loans.
        """
        return (
            f"[Card] ID: {self.card_number}, "
            f"Active Loans: {len(self.loan_queue)}"
        )
