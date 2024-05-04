import pandas

# class Students():

# csv_file = "updated_student_data.csv"
csv_file = "updated_student_data_sample.csv"
students_data_list = []
students_data = []

def get_csv_data():
    students_data_file = pandas.read_csv(csv_file)
    students_data = students_data_file.to_dict()
    data = {}

    for i in range(len(students_data_file)):
        data[students_data_file['class'][i]] = students_data_file.iloc[i]
    print(data)
    # print(students_data)
    # print(students_data_file)
    # class_list = students_data_file['class'].tolist()
    # class_list = list(set(class_list)) # only getting the unique values of class.
    # # print((class_list))
    # for row in students_data_file.iterrows():
    #     row_list = row[1].tolist()
    #     students_data.append(row_list)
    # # print(students_data_file.name.to_list())
    # # students_data_list = students_data_file.class.to_list()
    # # print(students_data)
    # # for eachClass in class_list:
    #     # print(eachClass)
    # for each in range(len(students_data)):
    #     # print(each, "--> ", students_data[each])
    #     for eachClass in class_list:
    #         if eachClass == students_data[each][4]:
    #             print(students_data[each][0])
    #     print('***********************')


# student = Students()
''' 1. Parse the data based on class| find the unique values of classes.
2. add this data to a list. Now based on the each class, filter out the students data.
3.  For each class get the name of the student based on ID.
4.  for each student ID, get the total marks for all subjects out of 500.
5.  save this date to an associated array for each student based on ID and Name.
6.  compare the total marks of each student and find the maximum marks, based on the max marks, print the name of Topper.
7.  Repeat the above process for each class. 
'''
get_csv_data()
