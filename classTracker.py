import datetime

class subject:
    def __init__(self, code, curAttendance):
        self.code = code
        self.schedule = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}
        self.totalClassTaken = curAttendance
        self.totalClassCount = 0
    
    def currentAttendance(self):
        """Returns the current attendace in percentage"""
        try:
            return 100*self.totalClassTaken/self.totalClassCount
        except ZeroDivisionError:
            return 0

    def addinitonalClassesReq(self):
        """Returns additional classes required to be attended to satisfy the 75% attendance criterion"""
        return ceil(0.75*self.totalClassCount-self.totalClassTaken)

def ceil(num):
    """Returns the tight integer upperbound of a number"""
    return int(-(-abs(num)//1)) if num > 0 else int(-abs(num)//1)

def dateRange(startDate, endDate):
    """Generator function"""
    for i in range(int((endDate-startDate).days)+1):
        yield startDate + datetime.timedelta(i)
    return

def dayName(day):
    "Returns day name corresponding to zero based indexing"
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return days[day]

def additionalReq(timeTable, subjectCodes, attendance, startDate, endDate, holidays = None):
    "Returns a dictionary of subject codes paired with additional classes required to be attended to satisfy the 75% attendance criterion in that particular subject"
    
    if holidays is None:
        holidays = []

    # ensuring that the inputs are of required type although it violates pythons philosophy i.e. "We're all consenting adults here"
    for arg in [timeTable, attendance]:
        if not isinstance(arg, dict):
            raise TypeError(f"Parameter {'timeTable' if arg is timeTable else 'attendance'} should be of type dict")

    for arg in [subjectCodes, holidays]:
        if not isinstance(arg, list):
             raise TypeError(f"Parameter {'subjectCodes' if arg is subjectCodes else 'holidays'} should be of type list")
    
    for arg in [startDate, endDate]:
        if not isinstance(arg, datetime.date):
             raise TypeError(f"Parameter {'startDate' if arg is startDate else 'endDate'} should be of type datetime.date")


    # container for subject instances
    subjects = {}
   
    # creating subject instances
    for code in subjectCodes:
        subjects[code] = subject(code, attendance[code]);
    
    # updating frequency of classes
    for day in timeTable.items():
        for subjectCode in day[1]:
            subjects[subjectCode].schedule[day[0]] += 1;

    # calculating total class count
    for date in dateRange(startDate, endDate):
        if(date in holidays):
            continue
        for sub in subjects.values():
            sub.totalClassCount += sub.schedule[dayName(date.weekday())]

    return {sub.code:sub.addinitonalClassesReq() for sub in subjects.values()}



if __name__ == "__main__":
    time_table = {
        "Monday": ['IT305', 'IT307', 'IT351'],
        "Tuesday": ['IT301', 'IT307', 'IT309', 'IT311', 'IT303', 'IT305'],
        "Wednesday": ['IT301', 'IT307', 'IT309', 'IT311', 'IT303', 'IT305'],
        "Thursday": ['IT301', 'IT307', 'IT355'],
        "Friday": ['IT301', 'IT305', 'IT303', 'IT353'],
        "Saturday": [],
        "Sunday": []
    }

    subject_list = []
    for day, classes in time_table.items():
        subject_list.extend(classes)

    subject_list = list(set(subject_list))
    subject_list.sort()

    attendance = {sub:0 for sub in subject_list}

    print(additionalReq(time_table, subject_list, attendance, datetime.date(22, 9, 19), datetime.date(22, 9, 25)))
