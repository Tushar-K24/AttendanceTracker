import datetime


weekdays_encode = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

weekdays_decode = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}
weekdays_limit = {i:0 for i in range(7)}

'''
Input:

time_table -> a dictionary mapping days with classes
e.g.,
{
"Monday": ['IT301', 'IT311'],
"Tuesday": ['IT311', 'IT321'],
...
}

classes -> a dictionary mapping classes and the no. of classes needed for an attendance of 75%.
e.g.,
{
"IT301": 10,
"IT351": 7,
...
}


Output: 

Version 1: returns a dictionary with days mapped with the count. 
e.g.,
{
"Monday": 5,
"Tuesday": 0,
"Wednesday": 7,
...
}
Which means that you need to attend all the classes for 5 mondays, you don't need to come on tuesdays, you need to attend all classes for 7 mondays, and so on.
'''


def dateRange(startDate, endDate):
    """Generator function"""
    for i in range(int((endDate-startDate).days)+1):
        yield startDate + datetime.timedelta(i)
    return

#code
def schedule(timeTable, classes, startDate, endDate):

    minDays, bestSchedule = 365, {}
    schedule = {}
    for weekday in weekdays_encode:
        schedule[weekday] = 0
      
    for date in dateRange(startDate, endDate):
      weekdays_limit[date.weekday()] += 1
      
    def classesRequired(remainingClasses):
        #returns true if classes are required to be attended
        for subject, cnt in remainingClasses.items():
            if cnt > 0:
                return True
        return False

    def minimizeDays(remainingClasses, currentDay, days, currentSchedule):
        nonlocal minDays, bestSchedule

        if not classesRequired(remainingClasses):
            #no more classes are required
            if days < minDays:
                minDays = days
                bestSchedule = currentSchedule.copy()
            return

        if currentDay > 6:
            #couldn't reach optimal solution
            return

        #skip cur_day
        minimizeDays(remainingClasses, currentDay + 1, days, currentSchedule)

        #attend every class on cur_day
        need = False
        for subj in timeTable[weekdays_decode[currentDay]]:
            if remainingClasses[subj] > 0:
                need = True
            remainingClasses[subj] -= 1

        currentSchedule[weekdays_decode[currentDay]] += 1

        if currentSchedule[weekdays_decode[currentDay]] > weekdays_limit[currentDay]:
          need = False
        if need:
            minimizeDays(remainingClasses, currentDay, days + 1, currentSchedule)

        for subj in timeTable[weekdays_decode[currentDay]]:
            remainingClasses[subj] += 1

        currentSchedule[weekdays_decode[currentDay]] -= 1

    #find best schedule
    minimizeDays(classes, 0, 0, schedule)

    return bestSchedule


if __name__ == "__main__":
    timeTable = {
      "Monday": ['IT305', 'IT307', 'IT351'],
      "Tuesday": ['IT301', 'IT307', 'IT309', 'IT311', 'IT303', 'IT305'],
      "Wednesday": ['IT301', 'IT307', 'IT309', 'IT311', 'IT303', 'IT305'],
      "Thursday": ['IT301', 'IT307', 'IT355'],
      "Friday": ['IT301', 'IT305', 'IT303', 'IT353'],
      "Saturday": [],
      "Sunday": []
    }

    classes = {'IT301': 13, 'IT303': 9, 'IT305': 12, 'IT307': 12, 'IT309': 5, 'IT311': 5, 'IT351': 2, 'IT353': 3, 'IT355': 3}

    
    for date in dateRange(datetime.date(22, 12, 1), datetime.date(23, 1, 1)):
      weekdays_limit[date.weekday()] += 1
      
    bestSchedule = schedule(timeTable, classes)
    print(bestSchedule)
