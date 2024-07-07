'''Problem Description
Given an integer A.
Two numbers, X and Y, are defined as follows:

X is the greatest number smaller than A such that the XOR sum of X and A is the same as the sum of X and A.
Y is the smallest number greater than A, such that the XOR sum of Y and A is the same as the sum of Y and A.
Find and return the XOR of X and Y.'''

import sys

A = 9
A_len= len(bin(A)[2:])
# print(A_len)

def CheckBit(N, i):
    if N & (1 << i) == 0:
        return False
    else:
        return True
    

x =0
y =0

for i in range(A_len-1, -1, -1):
    if CheckBit(A, i) == False:
        # print('unset bit: ', i)
        x = x | (1 << i)


y = 2**A_len
print('x:', x,'y: ',  y)
print('xor of x, y, :', x^y)