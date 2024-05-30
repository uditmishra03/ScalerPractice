"""Problem Description
You are given an array A of length N and Q queries given by the 2D array B of size Q×2.

Each query consists of two integers B[i][0] and B[i][1].

For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]]."""

# Input 1:
A = [1, 2, 3, 4, 5]
B = [[0, 2], [2, 4], [1, 4]]
# Input 2:
# A = [2, 1, 8, 3, 9, 6]
# B = [[0, 3],
#      [3, 5],
#      [1, 3],
#      [2, 4]]
print(A)
evennum = [0] * len(A)
# print(evennum)

for i in range(1, len(A)):
    # print(A[i])
    if A[0] % 2 == 0:
        evennum[0] = 1
    if A[i] % 2 == 0:
        # print(f"{i}: yes even number")#, evennum[i], evennum[i-1])
        evennum[i] = evennum[i - 1] + 1
    else:
        evennum[i] = evennum[i - 1]

print(evennum)


def findevenCount(arr, queries):
    results = [0] * len(B)
    for j in range(len(queries)):
        L, R = queries[j][0], queries[j][1]
        print(L, R)
        if L == 0:
            results[j] = evennum[R]
        else:
            results[j] = evennum[R] - evennum[L - 1]

    # print(results)
    return results


print(findevenCount(A, B))
