'''Problem Description
Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.

If the given array contains a sub-array with sum zero return 1, else return 0.'''

# A = [1, 2, 3, 4, 5]
A = [4, -1, 1]

# Create a prefix Array


def findZeroSumSubarray(A):
    pfsum = [0]*len(A)
    pfsum[0] = A[0]
    for i in range(1, len(A)):
        pfsum[i] = pfsum[i-1] + A[i]

    print('pfsum:', pfsum)

    for i in pfsum:
        if i == 0:
            return 1
    
    freq = {}
    for i in pfsum:
        if i not in freq:
            freq[i] =1
        else:
            return 1
    return 0
    

print(findZeroSumSubarray(A))

