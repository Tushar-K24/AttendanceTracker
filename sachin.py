import datetime
from math import ceil
'''
time_table -> a dictionary mapping days with classes
e.g.,
{
"Monday": ['IT301', 'IT311'],
"Tuesday": ['IT311', 'IT321'],
...
}
'''


class subject:

    def __init__(self, name, code, curAttendance):
        self.name = name
        self.code = code
        self.schedule = [0, 0, 0, 0, 0, 0, 0]
        self.totalClassTaken = curAttendance
        self.totalClassCount = 0

    def currentAttendance(self):
        return 100 * self.totalClassTaken / self.totalClassCount

    def addinitonalClassesReq(self):
        return ceil(0.75 * self.totalClassCount - self.totalClassTaken)


def dateRange(startDate, endDate):
    """Generator function"""
    for i in range(int((endDate - startDate).days) + 1):
        yield startDate + datetime.timedelta(i)
    return


def dayName(day):
    days = [
        "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
        "sunday"
    ]
    return days[day]


if __name__ == "__main__":

    print("NOTE: Enter dates in DD/MM/YY fromat.\n")

    startDate = datetime.datetime.strptime(
        input("Enter date of commencement of classes: "), "%d/%m/%y")
    endDate = datetime.datetime.strptime(
        input("Enter date of completion of classes: "), "%d/%m/%y")

    subjects = {}
    holidays = []

    n = int(input("Number of holidays during the semester: "))
    for i in range(n):
        date = input(f"Enter date of holiday {1}: ")
        holidays.append(datetime.datetime.strptime(date, "%d/%m/%y"))

    print(
        "\nNOTE: While entering number of classes, please enter it with respect to the duration of shortest class (i.e. class slot). For example if the shortest class is of 1 hours then a class taught for 2 hours would be counted as 2 classes.\n"
    )

    # adding subject data
    n = int(input("Enter total number of subjects: "))
    for i in range(n):
        print(f"\nEnter data for subject {i+1}")
        code = input("Enter subject code: ")
        name = input("Enter subject name: ")
        attended = int(input("Enter number of classes attended: "))
        subjects[code] = subject(name, code, attended)

    # retrieving information from time-table
    for day in range(7):
        n = int(
            input(f"Enter number of class slots taught on {dayName(day)}: "))
        for i in range(n):
            code = input(f"Enter subject code for slot {i+1}: ")
            subjects[code].schedule[day] += 1

    # calculating total number of classes for each subject
    for date in dateRange(startDate, endDate):
        if (date in holidays):
            continue
        for sub in subjects.values():
            sub.totalClassCount += sub.schedule[date.weekday()]

    # displaying result
    for sub in subjects.values():
        print(sub.name)
        print(f"current attendance: {sub.currentAttendance()}")
        print(f"Additional classes required: {sub.addinitonalClassesReq()}")
