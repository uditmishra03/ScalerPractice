'''Problem Description
Given a 2D Matrix A of dimensions N*N, we need to return the sum of all possible submatrices.'''

# A = [ [1, 1],
#       [1, 1] ]

A = [ [1, 2],
      [3, 4] ]

def getSubMatrixSum(A):
    n = len(A)

    ans = 0
    for i in range(n):
        for j in range(n):
            topLeft = (i+1)*(j+1)
            bottomRight = (n-i)*(n-j)
            num_sum = topLeft * bottomRight
            ans += num_sum* A[i][j]

    return ans

print(getSubMatrixSum(A))