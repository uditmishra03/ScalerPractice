"""Exercise 7: Check if two sets have any elements in common. If yes, display the common elements
Given:"""

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# print(set1 & set2)
if set1 & set2:
    print("Two sets has common element")
    print(set1 & set2)
else:
    print("Two sets has no common element")