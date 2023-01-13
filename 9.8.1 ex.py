class Duration:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __eq__(self, other):
        return (self.hours == other.hours) and (self.minutes == other.minutes)

monday_time = Duration(9, 0)
workday = Duration(10, 30)
tuesday_time = Duration(10, 30)

print(monday_time == workday)
print(tuesday_time == workday)
