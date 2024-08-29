

# A = [2, 3, 3]
A = [3,	3,	1,	1,	8,	8,	10,	10,	19, 19, 7,	6,	6,	2,	2,	4,	4]
def findUnique(arr):
    n = len(arr)

    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]

    lo = 1
    hi = n-2

    while lo <= hi:
        mid = (lo+hi)//2

        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        elif arr[mid] == arr[mid+1]:        #first occurnace
            if mid % 2 == 0:
                lo= mid+2
            else:
                hi = mid-1
        else:                               #second occurnace
            if mid % 2 == 0:
                hi= mid-2
            else:
                lo = mid+1



print('Final ans:', findUnique(A))
        