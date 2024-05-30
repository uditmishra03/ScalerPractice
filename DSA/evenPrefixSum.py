"""Problem Description
You are given an array A of length N and Q queries given by the 2D array B of size Q×2.

Each query consists of two integers B[i][0] and B[i][1].

For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]]."""

# Input 1:
# A = [1, 2, 3, 4, 5]
# B = [[0, 2],[2, 4], [1, 4]]
# Input 2:
A = [2, 1, 8, 3, 9, 6]
B = [[0, 3],
     [3, 5],
     [1, 3],
     [2, 4]]


# evenPrefixSum = [A[0]]
# for i in range (1, arraysize):
#     if i % 2 == 0:
#         evenPrefixSum.append(evenPrefixSum[i - 1] + A[i])
#     else:
#         evenPrefixSum.append(evenPrefixSum[i - 1])
#
# print(evenPrefixSum)

def findevenCount(arr, queries):
    # arraysize = len(arr)
    # print(queries)
    len_queries = len(queries)
    results = []
    for j in range(len_queries):
        # print(queries[j])
        L, R = queries[j][0], queries[j][1]
        evenCount = 0
        for k in range(L, R + 1):
            if arr[k] % 2 == 0:
                evenCount += 1
        results.append(evenCount)

    # print(results)
    return results


print(findevenCount(A, B))
