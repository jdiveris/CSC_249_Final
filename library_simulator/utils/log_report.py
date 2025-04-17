class LogReport:
    """
    Tracks and manages all major logging events during the simulation.
    Supports real-time logging of checkouts, returns, holds, and pickups,
    as well as daily summaries and an end-of-simulation report.
    """

    def __init__(self):
        """
        Initializes all log categories:
        - daily_logs: logs for the current day
        - checkout_log: all successful checkouts
        - return_log: all returns
        - hold_log: all hold placements
        - pickup_log: all successful hold pickups
        """
        self.daily_logs = []
        self.checkout_log = []
        self.return_log = []
        self.hold_log = []
        self.pickup_log = []

    def log_event(self, message):
        """
        Logs a generic event to the daily summary.

        Args:
            message (str): A description of the event.
        """
        self.daily_logs.append(message)

    def log_checkout(self, card_number, title):
        """
        Logs a successful book checkout.

        Args:
            card_number (str): The ID of the patron checking out the book.
            title (str): The title of the book being checked out.
        """
        message = f"{card_number} checked out \"{title}\""
        self.checkout_log.append(message)
        self.log_event(message)

    def log_hold(self, card_number, title):
        """
        Logs when a hold is placed on a book.

        Args:
            card_number (str): The ID of the patron placing the hold.
            title (str): The title of the book being held.
        """
        message = f"{card_number} placed a hold for \"{title}\""
        self.hold_log.append(message)
        self.log_event(message)

    def log_return(self, card_number, title):
        """
        Logs when a book is returned.

        Args:
            card_number (str): The ID of the patron returning the book.
            title (str): The title of the book being returned.
        """
        message = f"{card_number} returned \"{title}\""
        self.return_log.append(message)
        self.log_event(message)

    def log_pickup(self, card_number, title):
        """
        Logs when a held book is picked up.

        Args:
            card_number (str): The ID of the patron picking up the hold.
            title (str): The title of the book being picked up.
        """
        message = f"{card_number} picked up \"{title}\""
        self.pickup_log.append(message)
        self.log_event(message)

    def log_day_summary(self, day):
        """
        Prints and clears the current day's log summary.

        Args:
            day (int): The current day of the simulation.
        """
        print(f"\n=== End of Day {day} Summary ===")
        for message in self.daily_logs:
            print(f"- {message}")
        print("============================\n")
        self.daily_logs.clear()

    def log_end_of_simulation(self):
        """
        Prints a summary of total activity across the simulation.
        """
        print("\n=== End of Simulation Report ===")
        print(f"Total Checkouts: {len(self.checkout_log)}")
        print(f"Total Returns: {len(self.return_log)}")
        print(f"Total Holds Placed: {len(self.hold_log)}")
        print(f"Total Pickups: {len(self.pickup_log)}")
        print("===============================\n")