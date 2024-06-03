'''Problem Description
You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.........
But the sum must not exceed B.'''

A = 5
B = 12
C = [2, 1, 3, 4, 5]

n = len(A)
max = C[0]

# for i in range(n):
#     contri