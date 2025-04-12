class PickupRequest:
    """
    Represents a request by a library_card to pick up one or more available holds.
    Each hold in the list must be processed individually.
    """

    def __init__(self, library_card, holds_to_pickup):
        """
        Initializes a new PickupRequest with the library_card and a list of available holds.

        Args:
            library_card (LibraryCard): The patron picking up their reserved holds.
            holds_to_pickup (List[Hold]): A list of Hold objects available for pickup.
        """
        self.library_card = library_card
        self.holds_to_pickup = holds_to_pickup
        # Set a size attribute equal to the length of holds_to_pickup
        self.remaining_pickups = len(holds_to_pickup)

    def is_complete(self):
        """
        Checks whether all holds in the pickup request have been processed.

        Returns:
            bool: True if no holds remain; False otherwise.
        """
        return self.remaining_pickups <= 0

    def fetch_hold(self):
        """
        Retrieves and removes the next hold from the pickup list.

        Returns:
            Hold: The next Hold object to be processed.

        Raises:
            IndexError: If there are no remaining holds to fetch.
        """
        # If there are no holds to fetch, raise error
        if self.holds_to_pickup <= 0:
            raise IndexError("There are no available holds.")

        # Get hold from the holds list (removing it)
        hold = self.holds_to_pickup.pop()
        # Update remaining pickup quantity
        self.remaining_pickups = len(self.holds_to_pickup)

        # Return the fetched hold
        return hold
