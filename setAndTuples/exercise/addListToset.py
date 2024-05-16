"""Exercise 1: Add a list of elements to a set
Given a Python list, Write a program to add all its elements into a given set.


AD
Given:

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]"""

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

# for each in sample_list:
#     sample_set.add(each)
#
# print(sample_set)

sample_set.update(sample_list)
print(sample_set)
