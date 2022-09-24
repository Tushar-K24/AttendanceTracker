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


#code
def schedule(time_table, classes):

    def classes_required(remaining_classes):
        #returns true if classes are required to be attended
        for subject, cnt in remaining_classes.items():
            if cnt > 0:
                return True
        return False

    def minimize_days(remaining_classes, cur_day, days, cur_schedule):
        nonlocal min_days, best_schedule

        if not classes_required(remaining_classes):
            #no more classes are required
            if days < min_days:
                min_days = days
                best_schedule = cur_schedule.copy()
            return

        if cur_day > 6:
            #couldn't reach optimal solution
            return

        #skip cur_day
        minimize_days(remaining_classes, cur_day + 1, days, cur_schedule)

        #attend every class on cur_day
        need = False
        for subj in time_table[weekdays_decode[cur_day]]:
            if remaining_classes[subj] > 0:
                need = True
            remaining_classes[subj] -= 1

        cur_schedule[weekdays_decode[cur_day]] += 1

        if need:
            minimize_days(remaining_classes, cur_day, days + 1, cur_schedule)

        for subj in time_table[weekdays_decode[cur_day]]:
            remaining_classes[subj] += 1

        cur_schedule[weekdays_decode[cur_day]] -= 1

    min_days, best_schedule = 365, {}
    schedule = {}
    for weekday in weekdays_encode:
        schedule[weekday] = 0

    #find best schedule
    minimize_days(classes, 0, 0, schedule)

    print(min_days)
    return best_schedule


#test
time_table = {
    "Monday": ['IT1', 'IT2', 'IT3'],
    "Tuesday": ['IT3', 'IT4', 'IT5'],
    "Wednesday": [],
    "Thursday": ['IT1', 'IT2', 'IT4'],
    "Friday": ['IT5', 'IT6'],
    "Saturday": [],
    "Sunday": []
}

classes = {"IT1": 2, "IT2": 2, "IT3": 6, "IT4": 2, "IT5": 4, "IT6": 0}

best_schedule = schedule(time_table, classes)
print(best_schedule)
