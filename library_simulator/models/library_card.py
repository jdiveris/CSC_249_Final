from library_simulator.queues.list_queue import ListQueue


class LibraryCard:
    def __init__(self, card_number):
        self.card_number = card_number
        self.loan_queue = ListQueue()


    # def finish_book(self):
    #     # TODO: Implement function to initiate book return
    #     pass
    #
    # def get_a_book(self):
    #     # TODO: Implement function to initiate book checkout
    #     pass
