class Clock:
    """
    Tracks the passage of simulated time in hourly increments across days.
    """

    def __init__(self, hours_per_day=24):
        """
        Initializes a new simulation clock.

        Args:
            hours_per_day (int): The number of simulation ticks (hours) per simulated day.
        """
        self.current_day = 0
        self.current_hour = 0
        self.hours_per_day = hours_per_day

    def tick(self):
        """
        Advances the simulation clock by one hour.
        If the hour count exceeds the configured hours per day, the day is incremented
        and the hour resets to 0.
        """
        self.current_hour += 1
        if self.current_hour >= self.hours_per_day:
            self.current_hour = 0
            self.current_day += 1