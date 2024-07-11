'''Problem Description
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.'''

A = [2, 5, 6]
B = 10
n = len(A)
pfSum = [0]*n
pfSum[0]= A[0]
for i in range(1, n):
    pfSum[i] = pfSum[i - 1] + A[i]
print(pfSum)

count = 0
for i in range(n):
    for j in range(1, n):
        value = pfSum[j]
        if i >0:
            print(value, pfSum[i - 1], value-pfSum[i-1])
            value -= pfSum[i-1]
        if value < B:
            count +=1

print(count)