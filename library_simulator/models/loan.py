class Loan:
    """
    Represents a loaned book associated with a specific library card.

    Attributes:
        card_number (str): The ID of the library card that borrowed the book.
        isbn (str): The ISBN of the book being loaned.
        loan_period (int): The remaining loan period in days. Defaults to 14.
    """

    def __init__(self, card_number, isbn):
        """
        Initializes a Loan object with the associated card number and book ISBN.

        Args:
            card_number (str): The ID of the library card.
            isbn (str): The ISBN of the book being checked out.
        """
        self.card_number = card_number
        self.isbn = isbn
        self.loan_period = 14

    def decrement_loan_period(self):
        """
        Decreases the loan period by 1 day.
        """
        self.loan_period -= 1

    def is_elapsed(self):
        """
        Checks whether the loan period has expired.

        Returns:
            bool: True if the loan period has reached 0 or below, False otherwise.
        """
        return self.loan_period <= 0