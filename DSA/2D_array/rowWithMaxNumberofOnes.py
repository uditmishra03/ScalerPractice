'''Problem Description
Given a binary sorted matrix A of size N x N. Find the row with the maximum number of 1.

NOTE:

If two rows have the maximum number of 1 then return the row which has a lower index.
Rows are numbered from top to bottom and columns are numbered from left to right.
Assume 0-based indexing.
Assume each row to be sorted by values.
Expected time complexity is O(rows + columns).'''
#
# A = [   [0, 1, 1],
#          [0, 0, 1],
#          [0, 1, 1]  ]

A = [[0, 0, 0, 0],
     [0, 0, 0, 1],
     [0, 0, 1, 1],
     [0, 1, 1, 1]]


def findROwWithMaxOnes(mat):
    row = 0
    n = len(mat)
    col = n - 1
    ans = 0
    while row < n and col >= 0:
        while col >= 0 and mat[row][col] == 1:
            col -= 1
            ans = row
        row += 1

    return ans


print(findROwWithMaxOnes(A))
