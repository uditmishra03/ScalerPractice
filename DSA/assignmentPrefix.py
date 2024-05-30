"""Problem Description
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query."""

# A = [1, 2, 3, 4, 5]
# B = [[0, 3], [1, 2]]
# Input 2:
#
A = [2, 2, 2]
B = [[0, 0], [1, 2]]

def prefixSum(arr):
    prefixsum = []
    prefixsum.append(arr[0])
    # prefixsum[0] = arr[0]
    for i in range(1, len(arr)):
        prefixsum.append(prefixsum[i-1]+arr[i])
    return prefixsum


def findSum(pf, query):
    results = []
    for i in range(len(query)):
        # print(B[i])
        L, R = query[i][0], query[i][1]
        # print(L, R)
        if L == 0:
            sum = pf[R]
            results.append(sum)
        else:
            sum = pf[R]- pf[L-1]
            results.append(sum)
    return results


# print(prefixSum(A))
prefix_sum = prefixSum(A)
print(prefix_sum)
print(findSum(prefix_sum, B))
