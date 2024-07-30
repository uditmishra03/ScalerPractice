'''Given a sorted array of integers A (0-indexed) of size N, find the left most and the right most index of a given integer B in the array A.

Return an array of size 2, such that 
          First element = Left most index of B in A
          Second element = Right most index of B in A.
If B is not found in A, return [-1, -1].

Note : Your algorithm's runtime complexity must be in the order of O(log n).'''

# A = [5, 7, 7, 8, 8, 10]
# B = 8
# A = [5, 17, 100, 111]
# B = 3
A = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10 ]
B = 10

def searchRange(arr, k):
    n = len(arr)
    ans = [-1, -1]
    if n == 1:
        return ans
    
    lo, hi = 0, n-1
    ans_left, ans_right = -1, -1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == k:
            # if mid == 0 or arr[mid-1] < k:
                ans_left = mid
                hi = mid-1
        elif arr[mid] < k:
            lo = mid+1
        else:
            hi = mid-1
        # print(mid)
    print('first occurance:', ans_left)
    
    lo, hi = 0, n-1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == k:
            # if mid == 0 or arr[mid-1] < k:
                ans_right = mid
                lo = mid+1
        elif arr[mid] < k:
            lo = mid+1
        else:
            hi = mid-1
        # print(mid)
    print('last occurance:', ans_right)
    return ans_left, ans_right


print('final ans: ', searchRange(A, B))