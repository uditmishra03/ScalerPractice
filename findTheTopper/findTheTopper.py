import csv
from collections import defaultdict

# class Students():

csv_file = "updated_student_data.csv"
# csv_file = "updated_student_data_sample.csv"
students_data_list = []
students_data = []

''' 1. Parse the data based on class| find the unique values of classes.
2. add this data to a list. Now based on the each class, filter out the students data.
3.  For each class get the name of the student based on ID.
4.  for each student ID, get the total marks for all subjects out of 500.
5.  save this date to an associated array for each student based on ID and Name.
6.  compare the total marks of each student and find the maximum marks, based on the max marks, print the name of Topper.
7.  Repeat the above process for each class. 
'''

def read_csv():
    data = []
    with open(csv_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        # print(reader)
        for row in reader:
            data.append({
                "name": row["name"],
                "id": int(row["id"]),
                "class": int(row["class"]),
                "marks": int(row["marks"])
            })
    return data

data_dict = read_csv()
# print(data_dict)

student_marks = defaultdict(int)
for student in data_dict:
    # print(student['id']['class'])
    # print(student)
    student_id = student['id']
    class_id = student['class']
    student_name = student['name']
    marks = student['marks']
    student_marks[(student_id, class_id, student_name)] += marks

# print(student_marks)
## Print the sum of marks for each student of each class with unique id
# for (student_id, class_id, student_name), total_marks in student_marks.items():
#     print(f"Student ID: {student_id}, Class: {class_id}, Student Name: {student_name},  Total Marks: {total_marks}")

classes = []
for each in range(len(list(student_marks.keys()))):
    classes.append((list(student_marks.keys())[each][1]))
classes = list(set(classes))
# print(classes)

class_toppers = defaultdict(lambda: (0, None, ''))

for eachClass in range(len(classes)):
    for eachStudent in range(len(list(student_marks))):
        current_topper_marks, current_topper_id, current_topper_name = class_toppers[classes[eachClass]]
        student_id = list(student_marks.keys())[eachStudent][0]
        clas = list(student_marks.keys())[eachStudent][1]
        name = list(student_marks.keys())[eachStudent][2]
        marks = list(student_marks.values())[eachStudent]
        if classes[eachClass] == clas:
            if current_topper_marks < marks:
                class_toppers[classes[eachClass]] = (marks, student_id, name)

# print(class_toppers)

for class_id, (topper_marks, topper_id, topper_name) in class_toppers.items():
    if topper_id is not None:
        print(f"Class {class_id}'s Topper Name: {topper_name}, ID: {topper_id}, scored Total Marks: {topper_marks}")
