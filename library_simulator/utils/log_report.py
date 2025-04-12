class LogReport:
    def __init__(self):
        self.daily_logs = []

    def log_event(self, message):
        print(message)  # Simple real-time console log
        self.daily_logs.append(message)

    def log_day_summary(self, day):
        print(f"\n=== End of Day {day} Summary ===")
        for message in self.daily_logs:
            print(f"- {message}")
        print("============================\n")
        self.daily_logs.clear()