arr = [2, 11, 3, 6, 17, 15, 10, 12, 14, 28, 24, 21, 16, 8, 18, 9, 2, 3, 1]

def findLocalMaxima(arr):
    n = len(arr)

    if n ==1:
        return arr[0]
    if arr[0] > arr[1]:
        return arr[0]
    if arr[n-1]> arr[n-2]:
        return arr[n-1]
    
    lo, hi = 1, n-2
    while lo <= hi :
        mid = (lo+hi)//2

        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return arr[mid]
        if arr[mid] > arr[mid-1]:
            lo = mid+1
        else:
            hi = mid-1

print(findLocalMaxima(arr))
