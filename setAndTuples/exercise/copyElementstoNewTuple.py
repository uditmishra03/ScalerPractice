"""Exercise 6: Copy specific elements from one tuple to a new tuple
Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

Given:

tuple1 = (11, 22, 33, 44, 55, 66)"""

tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[3:-1]

print(type(tuple2))
print(tuple2)

tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222

print(tuple1)