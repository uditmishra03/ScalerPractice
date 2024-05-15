'''Exercise 8: Find all occurrences of a substring in a given string by ignoring the case'''

'''Write a program to find all occurrences of “USA” in a given string ignoring the case.

Given:

str1 = "Welcome to USA. usa awesome, isn't it?"'''

str1 = "Welcome to USA. usa awesome, isn't it?, usa, USa, US"
t_str1 = str1.lower()
checkFor = "USA"
# print(checkFor.lower(), checkFor.upper())

string_count = 0
if checkFor.lower() in t_str1:
    string_count = t_str1.count(checkFor.lower())

print(string_count)
