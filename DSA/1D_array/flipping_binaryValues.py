'''Problem Description
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d'''
import sys

A = "111"

print('Original String: ', A)

n = len(A)
l, r , cSum, maxSum = 0, 0, 0, 0
ans=[0]*2

for i in range(n):
    if A[i] == '1':
        cSum -=1
    if A[i] == '0':
        cSum +=1

    if cSum > maxSum:
        maxSum = cSum
        ans[0] = l+1
        ans[1] = r+1

    if cSum < 0:
        cSum = 0
        l = i+1
        r = i+1
    else:
        r +=1

if maxSum == 0:
    noans = []
    print(noans)
    # print('No solution found')
else:
    print(ans)