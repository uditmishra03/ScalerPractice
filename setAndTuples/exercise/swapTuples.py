"""Exercise 5: Swap two tuples in Python
Given:

tuple1 = (11, 22)
tuple2 = (99, 88)"""

tuple1 = (11, 22)
tuple2 = (99, 88)
print('Before swap: ')
print(tuple1)
print(tuple2)

# using the concept of unpacking.
tuple1, tuple2 = tuple2, tuple1

print('After swap: ')
print(tuple1)
print(tuple2)
#
# a , b = tuple2
# print(a, b)