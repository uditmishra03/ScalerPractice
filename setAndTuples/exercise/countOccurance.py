"""Exercise 9: Counts the number of occurrences of item 50 from a tuple"""

tuple1 = (50, 10, 60, 70, 50)

print(tuple1.count(50))

"""Exercise 10: Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)"""

tuple1 = (45, 45, 45, 45)


def checkIdentical(tup):
    allSame = True
    for each in tuple1:
        if each != tuple1[0]:
            allSame = False

    return allSame


result = checkIdentical(tuple1)
print(result)
