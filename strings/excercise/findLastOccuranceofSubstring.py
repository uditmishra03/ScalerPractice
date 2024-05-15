'''Exercise 12: Find the last position of a given substring
Write a program to find the last position of a substring “Emma” in a given string.'''

str1 = "Emma is a data scientist who knows Python. Emma works at google."

# print(str1.find('Emma'[::-1]))

# Both will do the job.
print(str1.rindex('Emma'))
print(str1.rfind('Emma'))