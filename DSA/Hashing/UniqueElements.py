'''Problem Description
Given an array A of N integers, return the number of unique elements in the array.'''

A = [3, 4, 3, 6, 6]

ans = set()

for each in A:
    ans.add(each)

print(ans, len(ans))
