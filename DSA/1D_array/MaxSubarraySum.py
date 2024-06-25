'''Problem Description
Find the maximum sum of contiguous non-empty subarray within an array A of length N.'''
import math

# A = [1, 2, 3, 4, -10]
# Input 2:
A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

ans = -math.inf
sum = 0

for i in range(len(A)):
    print(A[i], 'sum:', sum)
    sum += A[i]
    if sum > ans:
        ans = sum
    if sum < 0:    # Checking if sum is negative, if yes, then reset the sum to 0
        sum =0

print(ans)
