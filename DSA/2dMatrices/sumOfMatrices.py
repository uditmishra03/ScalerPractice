'''Problem Description
You are given two matrices A & B of same size, you have to return another matrix which is the sum of A and B.
Note: Matrices are of same size means the number of rows and number of columns of both matrices are equal.
The Following will give you an idea of matrix addition:'''

# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# B = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]

A = [[1, 2, 3],
     [4, 1, 2],
     [7, 8, 9]]

B = [[9, 9, 7],
     [1, 2, 4],
     [4, 6, 3]]

sumOfMatrices = []

n = len(A)
m = len(A[0])

for i in range(n):
    row = []
    for j in range(m):
        row.append(A[i][j]+B[i][j])
    sumOfMatrices.append(row)

print(sumOfMatrices)