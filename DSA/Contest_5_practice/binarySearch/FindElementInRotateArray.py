arr = [4, 5, 6, 8, 1, 2, 3]
k = 1

def findItem(arr, k):
    n = len(arr)
    lo , hi = 0, n-1

    while lo <= hi:
        mid = (lo+hi)//2

        if arr[mid] == k:
            return mid

        if arr[mid] >= arr[0]:
            if arr[0] <= k <= arr[mid]:
                hi = mid-1
            else:
                lo = mid+1
        else:
            if arr[mid] <= k <= arr[n-1]:
                lo = mid+1
            else:
                hi = mid-1

print('Final ans:', findItem(arr, k))