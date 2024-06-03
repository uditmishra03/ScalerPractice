'''Problem Description
You are given an integer array A of length N.
You have to find the sum of all subarray sums of A.
More formally, a subarray is defined as a contiguous part of an array which we can obtain by deleting zero or more elements from either end of the array.
A subarray sum denotes the sum of all the elements of that subarray.

Note : Be careful of integer overflow issues while calculations. Use appropriate datatypes.'''

A = [1, 2, 3]
n = len(A)
ans = 0
for i in range(n):
    contribution = (i+1)*(n-i)
    print(A[i], contribution)
    ans += A[i] * contribution

print(ans)