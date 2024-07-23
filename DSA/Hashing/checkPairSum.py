'''Problem Description
Given an Array of integers B, and a target sum A.
Check if there exists a pair (i,j) such that Bi + Bj = A and i!=j.'''

A = 4
B = [3, 5, 1, 2, 1, 2]

def checkPairSum(k, arr):
    freq = {}
    for i in range(len(arr)):
        target = k-arr[i]
        print('element:', arr[i], 'Target:', target)
        if target in freq:
            return 1
        else:
            freq[arr[i]] =1
    return 0

print(checkPairSum(A, B))