'''You are given an array A of N integers and an integer B.
Count the number of pairs (i,j) such that A[i] - A[j] = B and i ≠ j.

Since the answer can be very large, return the remainder after dividing the count with 109+7.'''


from collections import defaultdict


A = [3, 5, 1, 2]
B = 4

# A = [1, 2, 1, 2]
# B = 1
def CountPairDiff(arr, k):
    freq = defaultdict(int)
    # freq = {}
    mod = (10**9+7)
    count = 0
    for i in range(len(arr)):
        diff_target = arr[i]-k
        sum_target = k+arr[i]
        if diff_target in freq: 
            count += freq[diff_target]
        if sum_target in freq:
            count += freq[sum_target]
        # print('element:', arr[i], 'Target:', target)
        # if diff_target in freq:
        # count = (count + freq[diff_target] + freq[sum_target]) % mod
        freq[arr[i]] +=1
    return int(count % mod)


print('final ans:', CountPairDiff(A, B))