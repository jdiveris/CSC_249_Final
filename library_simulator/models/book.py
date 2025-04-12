from library_simulator.queues.list_queue import ListQueue


class Book:
    """
    Represents a book in the library collection, tracking copies, availability,
    and any holds placed by cardholders.
    """

    def __init__(self, isbn, author, title, total_copies):
        """
        Initializes a new Book object.

        Args:
            isbn (str): The book's unique ISBN.
            author (str): The author's name.
            title (str): The title of the book.
            total_copies (int): The total number of copies the library owns.
        """
        self.isbn = isbn
        self.author = author
        self.title = title
        self.total_copies = total_copies
        self.available_copies = total_copies
        self.hold_queue = ListQueue()

    def __str__(self):
        """
        Returns a formatted string representation of the book.

        """
        # TODO: Create a proper str representation
        pass

    def is_available(self):
        """
        Checks whether there are any available copies of the book.

        Returns:
            bool: True if at least one copy is available; False otherwise.
        """
        return self.available_copies > 0

    def has_holds(self):
        """
        Checks whether there are any active holds on the book.

        Returns:
            bool: True if the hold queue is not empty; False otherwise.
        """
        return not self.hold_queue.is_empty()

    def __repr__(self):
        return f"<Book title='{self.title}', isbn='{self.isbn}', available={self.available_copies}/{self.total_copies}>"


    def __str__(self):
        return (
            f"[Book] Title: '{self.title}', ISBN: {self.isbn}, "
            f"Author: {self.author}, Available: {self.available_copies}/{self.total_copies}, "
            f"Holds: {len(self.hold_queue)}"
        )