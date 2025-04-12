class Loan:
    def __init__(self, card_number, isbn):
        self.card_number = card_number
        self.isbn = isbn
        self.loan_period = 14

    def decrement_loan_period(self):
        self.loan_period -= 1

    def is_elapsed(self):
        return self.loan_period <= 0