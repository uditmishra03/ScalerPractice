'''Problem Description
Given an array of integers A, find and return the peak element in it.
An array element is considered a peak if it is not smaller than its neighbors. For corner elements, we need to consider only one neighbor.

NOTE:

It is guaranteed that the array contains only a single peak element.
Users are expected to solve this in O(log(N)) time. The array may contain duplicate elements.'''

# A = [1, 2, 3, 4, 5, 7, 9]
# A = [5, 17, 100, 11]
A = [1,1000000000,1000000000]


def findPeakelement(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n-1] > arr[n-2]:
        return arr[n-1]
    lo, hi = 1, n-2
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] >= arr[mid-1] and arr[mid] >= arr[mid+1]:
            return arr[mid]
        elif arr[mid] > arr[mid-1]:    # moving right
            lo = mid+1
        else:
            hi = mid-1
    
print('final ans: ', findPeakelement(A))
    