'''Problem Description
Given a vector A of non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.'''

# A = [0, 1, 0, 2]
# Input 2:
# A = [1, 2]
A = [2, 1,3, 2, 1,2,4,3,2,1,3,1]
n = len(A)
leftMax ,rightMax =[0]*n, [0]*n

leftMax[0] = A[0]
for i in range(1, n):
    leftMax[i] = max(leftMax[i-1], A[i])

print(leftMax)

rightMax[-1]= A[-1]
for i in range(n-2, -1, -1):
    rightMax[i] = max(rightMax[i+1], A[i])

print(rightMax)

water = 0
for i in range(1, n-1):
    left_support = leftMax[i-1]
    right_support = rightMax[i+1]
    netsupport = min(left_support, right_support)
    # print(f"for {i}: left support : {left_support} \nright support : {right_support} \nnetsupport : {netsupport}")
    if netsupport >= A[i]:
        water += netsupport-A[i]

print(f"water: {water}")