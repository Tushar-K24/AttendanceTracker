import datetime

time_table_24 = {
    "Monday": ['IT305', 'IT307', 'IT351'],
    "Tuesday": ['IT301', 'IT307', 'IT309', 'IT311', 'IT303', 'IT305'],
    "Wednesday": ['IT301', 'IT307', 'IT309', 'IT311', 'IT303', 'IT305'],
    "Thursday": ['IT301', 'IT307', 'IT355'],
    "Friday": ['IT301', 'IT305', 'IT303', 'IT353'],
    "Saturday": [],
    "Sunday": []
}
time_table_23 = {
    "Monday": ['IT407', 'IT413', 'IT411'],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": ['IT461', 'IT413', 'IT403','IT407'],
    "Friday": ['IT451', 'IT455', 'IT403', 'IT411'],
    "Saturday": [],
    "Sunday": []
}
time_table_25 = {
    "Monday": ['ICT207', 'ICT205', 'ICT201','ICT203','ICT209'],
    "Tuesday": ['ICT207', 'ICT205', 'ICT201', 'ICT203', 'ICT209'],
    "Thursday": ['ICT211', 'ICT205', 'ICT201', 'ICT209'],
    "Friday": ['ICT251', 'ICT211', 'ECO213','ICT253'],
    "Wednesday": [],
    "Saturday": [],
    "Sunday": []
}

time_table_db = {
    "CSE24": time_table_24,
    "CSE25": time_table_25,
    "CSE23": time_table_23
}

role_list = {'CSE23', 'CSE24', 'CSE25'}

academic_dates = {
    "CSE24": (datetime.date(22, 12, 1), datetime.date(23, 1, 1)),
    "CSE25": (datetime.date(22, 12, 1), datetime.date(23, 1, 1)),
    "CSE23": (datetime.date(22, 12, 1), datetime.date(23, 1, 1))
}


def getBatch(batch_id):
    time_table = time_table_db[batch_id]
    subject_list = []
    for day, classes in time_table.items():
        subject_list.extend(classes)
    subject_list = list(set(subject_list))
    subject_list.sort()
    return {
        'time_table': time_table,
        'subject_list': subject_list,
        'dates': academic_dates[batch_id]
    }
