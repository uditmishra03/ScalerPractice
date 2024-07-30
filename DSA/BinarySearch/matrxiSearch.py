'''Problem Description
Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that searches for integer B in matrix A.

This matrix A has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than or equal to the last integer of the previous row.
Return 1 if B is present in A, else return 0.

NOTE: Rows are numbered from top to bottom, and columns are from left to right.'''


# A = [ 
#       [1,   3,  5,  7],
#       [10, 11, 16, 20],
#       [23, 30, 34, 50] 
#     ]
# B = 2

A = [   
      [5, 17, 100, 111],
      [119, 120, 127, 131]    
    ]
B = 3

print(A)
def findinMatrix(A, B):
    n = len(A)
    m = len(A[0])
    # print(n, m)

    i = 0
    j = m-1
    # print(A[i][j])


    while i < n and j >= 0 :
        if A[i][j] == B:
            return 1
        elif A[i][j] > B:
            j -=1
        else:
            i +=1
    return 0
    
print(findinMatrix(A, B))