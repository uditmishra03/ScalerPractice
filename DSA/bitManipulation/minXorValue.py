import sys
'''Problem Description
Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.'''

# A = [ 2, 0, 5, 7]
A = [0, 4, 7, 9]

'''
1. sort the array.
2. Keep track of min xor value and try all the adjacent xor of elements.
'''
# print(A)
A.sort()
# print(A)

minXor= sys.maxsize

for i in range(1, len(A)):
    # print(A[i-1], A[i])
    xor = A[i-1]^ A[i]
    if minXor >xor :
        minXor = xor

print('Final ans:', minXor)