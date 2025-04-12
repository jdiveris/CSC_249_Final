from library_simulator.queues.list_queue import ListQueue


class LibraryCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.loan_queue = ListQueue()

    def __repr__(self):
        return f"<LibraryCard #{self.card_number}, loans={len(self.loan_queue)}>"

    def __str__(self):
        return (
            f"[Card] ID: {self.card_number}, "
            f"Active Loans: {len(self.loan_queue)}"
        )
