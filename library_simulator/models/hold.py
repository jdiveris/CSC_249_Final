class Hold:
    """
    Represents a hold placed by a library cardholder on a specific book.

    Attributes:
        isbn (str): The ISBN of the book on hold.
        card_number (str): The card number of the patron who placed the hold.
        fulfilled (bool): Whether the hold has been fulfilled (book picked up).
        time_to_claim (int): Remaining days to claim the held book.
    """

    def __init__(self, isbn, card_number):
        """
        Initializes a new Hold instance.

        Args:
            isbn (str): The ISBN of the book being held.
            card_number (str): The card number of the patron placing the hold.
        """
        self.isbn = isbn
        self.card_number = card_number
        self.fulfilled = False
        self.time_to_claim = None

    def decrement_time_to_claim(self):
        """
        Decrements the time remaining for the patron to claim the book.
        """
        self.time_to_claim -= 1

    def has_expired(self):
        """
        Checks whether the hold has expired based on time left.

        Returns:
            bool: True if the hold has expired; False otherwise.
        """
        return self.time_to_claim <= 0

    def __eq__(self, other):
        """
        Compares two Hold instances for equality.

        Args:
            other (Hold): The other hold to compare with.

        Returns:
            bool: True if ISBN and card number match; False otherwise.
        """
        if not isinstance(other, Hold):
            return NotImplemented
        return self.isbn == other.isbn and self.card_number == other.card_number

    def __repr__(self):
        """
        Returns a string representation of the Hold for debugging.

        Returns:
            str: A string showing the ISBN, card number, fulfillment status, and time remaining.
        """
        return f"<Hold isbn='{self.isbn}', card='{self.card_number}', fulfilled={getattr(self, 'fulfilled', False)}, time_left={self.time_to_claim}>"
