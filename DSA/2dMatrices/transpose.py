'''Problem Description
Given a 2D integer array A, return the transpose of A.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.'''

A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# A = [[1, 2],[1, 2],[1, 2]]

def print2Darray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end =' ')
        print()
res = []
n = len(A)
m = len(A[0])

print("Before transpose: ")
print2Darray(A)
for i in range(m):
    # print(i)
    row = []
    for eachrow in A:
        row.append(eachrow[i])
    res.append(row)

print("After transpose:")
print2Darray(res)