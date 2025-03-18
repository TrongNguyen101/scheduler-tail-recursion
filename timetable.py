class TimeTable:
    def __init__(self, subjects, timeslots, days):
        self.subjects = subjects
        self.timeslots = timeslots
        self.days = days
        self.table = [[None for _ in range(len(days))] for _ in range(len(timeslots))]

    def generate_timetable(self):
        # Example logic to fill the timetable with subjects
        for i, timeslot in enumerate(self.timeslots):
            for j, day in enumerate(self.days):
                if i < len(self.subjects):
                    self.table[i][j] = self.subjects[i].subjectCode
                else:
                    self.table[i][j] = "Free"

    def display_timetable(self):
        # Print the header
        col_width = 16
        print("Time/Day".ljust(col_width), end="")
        for day in self.days:
            print(day.day.ljust(col_width), end="")
        print()

        # Print the timetable
        for i, timeslot in enumerate(self.timeslots):
            print(f"{timeslot.start_time}-{timeslot.end_time}", end="\t")
            for j in range(len(self.days)):
                print(self.table[i][j], end="\t")
            print()