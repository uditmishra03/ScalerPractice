'''Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to create a staircase of max-height using these blocks.

The first stair would require only one block, and the second stair would require two blocks, and so on.

Find and return the maximum height of the staircase.'''

A = 100

def calcHeight(h):
    return (h**2 + h)//2

def findHeight(A):
    # print(calcHeight(5))
    lo = 1
    hi = A
    ans = 0

    while lo <= hi:
        mid = (lo+hi)//2
        if calcHeight(mid) == A:
            return mid
        if calcHeight(mid) < A:
            ans = max(ans, mid)
            lo = mid+1
        else:
            hi = mid-1
    return ans



print(findHeight(A))