"""Exercise 2: Return a new set of identical items from two sets
Given:

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}"""

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

result_set = set()

# for item in set1:
#     if item in set2:
#         result_set.add(item)

# print(set1.intersection(set2))
# print(result_set)
print(set1 & set2)
