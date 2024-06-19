'''Problem Description
You are given a n x n 2D matrix A representing an image.

Rotate the image by 90 degrees (clockwise).

You need to do this in place.

Note: If you end up using an additional array, you will only receive partial score.'''

# A = [[1, 2],[3, 4]]
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(A)
def print2Darray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end =' ')
        print()
print("Original Matrix: ")
print2Darray(A)
# 1. Take a transpose of matrix

def transposeMatrix(arr):
    n = len(arr)
    m = len(arr[0])
    transpose = []

    for i in range(m):
        row = []
        for j in range(n):
            row.append(arr[j][i])
        # print(f"row: {row}")
        transpose.append(row)
    return transpose


A = transposeMatrix(A)
print("After transpose: ")
print2Darray(A)

# 2. Reverse each row
for i in A:
    print(i.reverse())
print("After reversal: ")
print2Darray(A)
# print(A)