from subject import Subject
from timeslot import TimeSlot
from dayofweek import DayOnWeek

subjects = [
    Subject("COSC2531", "MobileProgramming"),
    Subject("COSC2532", "Web Programming"),
    Subject("COSC2533", "Data Science"),
    Subject("COSC2534", "Cloud Computing")
]

timeslots = [
    TimeSlot("7:00", "9:15"),
    TimeSlot("9:30", "11:45"),
    TimeSlot("13:00", "15:15"),
    TimeSlot("15:30", "17:45")
]

days = [
    DayOnWeek("Monday"),
    DayOnWeek("Tuesday"),
    DayOnWeek("Wednesday"),
    DayOnWeek("Thursday"),
    DayOnWeek("Friday")
]

print(subjects[0].subjectCode, subjects[0].subjectName)
print(subjects[1].subjectCode, subjects[1].subjectName)
print(subjects[2].subjectCode, subjects[2].subjectName)
print(subjects[3].subjectCode, subjects[3].subjectName)

print("\nTime Slots")
print(timeslots[0].start_time, timeslots[0].end_time)
print(timeslots[1].start_time, timeslots[1].end_time)
print(timeslots[2].start_time, timeslots[2].end_time)
print(timeslots[3].start_time, timeslots[3].end_time)

print("\nDays")
print(days[0].day)
print(days[1].day)
print(days[2].day)
print(days[3].day)
print(days[4].day)

// Thinking about how to generate a timetable following the above data structure
// I would create a class called Timetable
// I would create a method called generate_timetable