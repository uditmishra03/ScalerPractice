'''Problem Description
You are given a 2D integer matrix A, return a 1D integer array containing column-wise sums of original matrix.'''

# Input 1:
A=[[1,2,3,4],[5,6,7,8],[9,2,3,4]]

# print(A, len(A))
n = len(A)
m=len(A[0])
result = []
for j in range(m):
    sum = 0
    for i in range(n):
        # print(A[i][j], end=' ')
        sum += A[i][j] #print()
    # print(sum)
    result.append(sum)
print(result)