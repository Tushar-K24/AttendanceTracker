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
