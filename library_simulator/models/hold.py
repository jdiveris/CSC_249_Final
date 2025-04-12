class Hold:
    def __init__(self, isbn, card_number):
        self.isbn = isbn
        self.card_number = card_number
        self.available = False
        self.time_to_claim = None

    def decrement_time_to_claim(self):
        self.time_to_claim -= 1

    def has_expired(self):
        return self.time_to_claim <= 0
