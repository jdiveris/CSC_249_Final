class Hold:
    def __init__(self, isbn, card_number):
        self.isbn = isbn
        self.card_number = card_number
        self.available = False
        self.time_to_claim = None

    def decrement_time_to_claim(self):
        self.time_to_claim -= 1

    def time_to_claim_elapsed(self):
        # TODO: Implement code to delete hold once time has elapsed
        pass
