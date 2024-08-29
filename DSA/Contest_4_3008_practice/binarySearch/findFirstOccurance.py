def findFirstOccurance(arr, k):
    n = len(arr)

    lo = 0
    hi = n
    # count = 0
    ans = -1
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == k:
            ans = mid
            # print(ans)
            hi = mid-1
        elif arr[mid] < k:
            lo = mid+1
        else:
            hi = mid-1
    # print(count)
    return mid


arr = [-5,-5,-3,0,0,1,1,5,5,5,	5,	5,	5,	5,	8,	10,	10,	15,	15]

print(arr)
k = 5

print('final ans:', findFirstOccurance(arr, k))

print('final ans:', findFirstOccurance(arr, 15))