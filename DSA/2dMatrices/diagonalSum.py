'''Problem Description
You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.

Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.'''

arr = [[1, -2, -3], [-4, 5, -6], [-7 ,-8, 9]]

n = len(arr)
sum = 0
for i in range(n):
    sum += arr[i][i]
# print(sum)
print(sum)