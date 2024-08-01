'''Given an array of integers A and an integer B.
Find the total number of subarrays having sum equals to B'''
'''Return the total number of subarrays having sum equals to B.
'''

from collections import defaultdict


# A = [1, 0, 1]
# B = 1

A = [2, 3, 9 -4, 1, 5, 6, 2, 5]
B = 11
# A = [0, 0, 0]
# B = 0

def subArraySumEqualsK(arr, k):
    print('Original array: ', arr)
    print('k: ', k)
    n = len(arr)
    pfsum = [0]*n
    pfsum[0] = arr[0]
    for i in range(1, n):
        pfsum[i] = arr[i] + pfsum[i-1]

    print('prefix sum:', pfsum)
    subarray_count = 0

    freq = defaultdict(int)

    for i in range(n):
        if k == pfsum[i]:
            subarray_count +=1
        target = pfsum[i]-k
        print(freq, target)
        if target in freq:
            subarray_count += freq[target]

        freq[pfsum[i]] +=1       
    return subarray_count




print(subArraySumEqualsK(A, B))