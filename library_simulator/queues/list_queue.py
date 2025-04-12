class ListQueue:
    """
    A basic FIFO (first-in, first-out) queue implementation using a Python list.
    Supports enqueue, dequeue, and peek operations.
    """

    def __init__(self, sourcecollection=None):
        """
        Initializes a new ListQueue. Optionally fills the queue with items from an existing iterable.

        Args:
            sourcecollection (iterable, optional): Items to add to the queue initially.
        """
        self.items = []

        if sourcecollection:
            for item in sourcecollection:
                self.enqueue(item)

    def __len__(self):
        """
        Returns the number of items currently in the queue.

        Returns:
            int: The number of items.
        """
        return len(self.items)

    def __iter__(self):
        for item in self.items:
            yield item

    def is_empty(self):
        """
        Checks whether the queue is empty.

        Returns:
            bool: True if the queue has no items; False otherwise.
        """
        return len(self) == 0

    def enqueue(self, item):
        """
        Adds an item to the rear of the queue.

        Args:
            item: The item to be enqueued.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Removes and returns the item at the front of the queue.

        Returns:
            Any: The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("The Queue is empty.")

        item = self.peek()
        del self.items[0]

        return item

    def peek(self):
        """
        Returns the item at the front of the queue without removing it.

        Returns:
            Any: The item at the front of the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("The Queue is empty.")

        return self.items[0]

    def contains(self, target):
        """
        Checks if the target item exists in the queue.

        Args:
            target: The item to search for.

        Returns:
            bool: True if the item is in the queue, False otherwise.
        """
        return target in self.items

    def remove(self, target):
        """
        Removes the first occurrence of the specified item from the queue.

        Args:
            target: The item to remove from the queue.

        Raises:
            ValueError: If the item is not found in the queue.
        """
        if not target in self.items:
            raise ValueError("Item not in queue")

        self.items.remove(target)