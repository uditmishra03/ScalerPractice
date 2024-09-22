'''Problem Description
Given a matrix of integers A of size N x M and an integer B.
In the given matrix every row and column is sorted in non-decreasing order. Find and return the position of B in the matrix in the given form:
If A[i][j] = B then return (i * 1009 + j)
If B is not present return -1.'''
#
# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# B = 2
#
A = [[1, 2],
     [3, 3]]
B = 3
#
# A=[[1,3,5,7],[2,4,6,8]]
# B = 10

# A = [[2,8,8,8],[2,8,8,8],[2,8,8,8]]
# B = 8

# A = [[3,3,3],[3,3,3],[3,3,3]]
# B = 3
def searchAnElement(A,B):
    n = len(A)
    m = len(A[0])
    # print(n, m)
    min_i, min_j = n-1,m-1
    i, j=0,m-1
    while i < n and j >=0:
        # print(A[i][j])
        if A[i][j] == B:
            print('found it at position ',i+1,  j+1)
            min_i= min(min_i, i)
            min_j = min(min_j, j)
            for k in range(j, -1, -1):
                if A[i][k] == B:
                    min_j = min(min_j, k)
            # print('@line 37: ', min_j)
            ans = (min_i+1) * 1009+(min_j+1)
            # print(ans, min_i, min_j)
            return ans
        elif A[i][j] > B:
            j-=1
        else:
            i+=1
        # print(i, j)
    return -1

print(searchAnElement(A, B))