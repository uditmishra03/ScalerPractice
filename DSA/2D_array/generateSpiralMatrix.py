'''Problem Description
Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.'''

n = 5
ans = []
print(n)


def print2DMat(mat):
    for i in range(len(mat[0])):
        print(mat[i])
    # print()

if n == 0:
    mat = []
    print(mat)

mat = [row[:] for row in [[0]*n]*n]
print('Original matrix: ', mat)

i , j =0, 0
value = 1
while n> 1:
    for k in range(n-1):
        mat[i][j] = value
        value+=1
        j +=1
    print(print2DMat(mat))
    # print(i, j)
    for k in range(n-1):
        # print(k)
        # print(i, j, value)
        mat[i][j] = value
        value+=1
        i +=1
    print(print2DMat(mat))
    # print(i, j)
    for k in range(n-1):
        mat[i][j] = value
        value+=1
        j -=1
    print(print2DMat(mat))
    # print(i, j)
    for k in range(n-1):
        mat[i][j] = value
        value+=1
        i -=1
    print(print2DMat(mat))
    # print(i, j)
    i+=1
    j+=1
    n-=2

if n==1:
    mat[i][j] = value
print(mat)