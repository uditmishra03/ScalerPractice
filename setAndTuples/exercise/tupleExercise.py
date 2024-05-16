"""Exercise 1: Reverse the tuple
Given:
"""
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])

"""Exercise 2: Access value 20 from the tuple
The given tuple is a nested tuple. write a Python program to print the value 20."""

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])


"""Exercise 3: Create a tuple with single item 50"""

tup = (50, )
print(type(tup), tup)

"""Exercise 4: Unpack the tuple into 4 variables
Write a program to unpack the following tuple into four variables and display each variable.

Given:
"""
tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(a, b, c, d, sep = '|')