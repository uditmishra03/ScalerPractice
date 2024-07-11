'''Problem Description

Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.'''


import sys
# A = [8, 3, 10, 20, 22, 13,1,2,55, 5, 15, 50]
# B = 5
# A = [1, 12, 10, 3, 14, 10, 5]
# B = 8

A = [5, 17, 100, 11]
B = 20

ans = sys.maxsize

print("Original aarray: ", A)
smallNoCount = 0
for element in A:
    if element <= B:
        smallNoCount +=1

print('small no count: ', smallNoCount)

# Badelements --> elements larger than value of B
badElements = 0
for i in range(smallNoCount):
    # print(A[i])
    if A[i] > B:
        badElements +=1

ans = min(ans, badElements)
print('ans so far: ', ans)

start = 1
end = smallNoCount
# print(A[start: end+1])
while end < len(A):
    print('window: ', A[start: end+1])
    if A[start-1] > B:
        badElements -=1
    if A[end] > B:
        badElements +=1
    start +=1
    end +=1
    print("New Badelements: ", badElements)

    ans = min(ans, badElements)

print('Final ans : ', ans )