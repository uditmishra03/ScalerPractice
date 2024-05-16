"""Exercise 8: Sort a tuple of tuples by 2nd item
Given:
"""
tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
tap = tuple1[::-1]
# print(tap)
# tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))

tuple2 = sorted(tuple1, key = lambda x: x[1])
print(tuple1, tuple2, sep= '\n')
tap2 = sorted(tap, key = lambda x: x[0])
print(tap, tap2, sep='\n')

