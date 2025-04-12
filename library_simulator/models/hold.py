class Hold:
    def __init__(self, isbn, card_number):
        self.isbn = isbn
        self.card_number = card_number
        self.fulfilled = False
        self.time_to_claim = None

    def decrement_time_to_claim(self):
        self.time_to_claim -= 1

    def has_expired(self):
        return self.time_to_claim <= 0

    def __eq__(self, other):
        if not isinstance(other, Hold):
            return NotImplemented
        return self.isbn == other.isbn and self.card_number == other.card_number

    def __repr__(self):
        return f"<Hold isbn='{self.isbn}', card='{self.card_number}', fulfilled={getattr(self, 'fulfilled', False)}, time_left={self.time_to_claim}>"