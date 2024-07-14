'''
On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 0-indexed.)'''

import sys

sys.setrecursionlimit(10**6)

# A = 3
# B = 0
A = 4
B = 4

def findKthSymbol(a):
    if a == 1:
        return [0]
    arr = findKthSymbol(a-1)
    curr = []
    for i in range(0, len(arr)):
        if arr[i] == 0:
            curr.append(0)
            curr.append(1)
        else:
            curr.append(1)
            curr.append(0)
    
    return curr


arr= findKthSymbol(A)
print(arr)
print('Final ans:', arr[B])