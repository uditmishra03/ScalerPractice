"""Exercise 6: Return a set of elements present in Set A or B, but not both
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}"""


set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

print(set1 ^ set2)

print(set1.symmetric_difference(set2))