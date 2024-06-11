'''Problem Description
You are given a N X N integer matrix. You have to find the sum of all the minor diagonal elements of A.
Minor diagonal of a M X M matrix A is a collection of elements A[i, j] such that i + j = M + 1 (where i, j are 1-based).'''

# A = [[1, -2, -3],
#      [-4, 5, -6],
#      [-7, -8, 9]]

A=  A = [[3, 2],
      [2, 3]]
n = len(A)
m = len(A[0])
# print(n, m)

row = 0
col= m-1
# print(A[row][col])
sum = 0
while row <n and col >=0:
    # print(A[row][col])
    sum += A[row][col]
    row += 1
    col -=1
print(sum)