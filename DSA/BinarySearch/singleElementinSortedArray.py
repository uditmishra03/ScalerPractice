'''Problem Description
Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once.

Elements which are appearing twice are adjacent to each other.

NOTE: Users are expected to solve this in O(log(N)) time.'''


# A = [1, 1, 7]
A = [2, 3, 3]


def findSingleElement(arr):
    n = len(arr)

    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    lo, hi = 1, n-2
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        elif arr[mid] == arr[mid+1]:
            if mid % 2  !=0:
                hi = mid-1
            else:
                lo= mid+2
        else:
            if mid %2 != 0:
                lo = mid+1
            else:
                hi = mid-2


    


print(findSingleElement(A))