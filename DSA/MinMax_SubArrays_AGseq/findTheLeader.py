'''Problem Description
Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.

NOTE: The rightmost element is always a leader.'''

A = [16, 17, 4, 3, 5, 2]

results = []
max = A[-1]
results.append(max)
print(max, '***')

for i in range(len(A)-2, -1, -1):
    if A[i] > max:
        max = A[i]
        results.append(max)
print(results)
