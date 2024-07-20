'''Problem Description
Given an integer array A of size N, find the first repeating element in it.

We need to find the element that occurs more than once and whose index of the first occurrence is the smallest.

If there is no repeating element, return -1.'''

# A = [10, 5, 3, 4, 3, 5, 6]
A = [6, 10, 5, 4, 9, 120]

def findFirstRepeating(arr):
    freqArr = {}

    for i in arr:
        if i not in freqArr:
            freqArr[i] = 1
        else:
            freqArr[i] += 1
    
    for each in freqArr:
        if freqArr[each] >1:
            return each
    return -1


print(findFirstRepeating(A))