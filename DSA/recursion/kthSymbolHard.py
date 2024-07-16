
import sys

sys.setrecursionlimit(10**6)

A = 3
B = 0
# A = 4
# B = 4

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
    print(curr)
    return curr



# if A >=2:



arr_len = 2**(A-1)      
print('length:', arr_len)
mid=arr_len//2
print('mid:', mid)
arr= findKthSymbol(A-1)
print(arr)
if B <  mid:
    print('Final ans:', arr[B])
else:
    print('Final ans:   ', arr[B-mid]^1)

