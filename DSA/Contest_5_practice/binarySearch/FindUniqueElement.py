arr = [3, 3,7,  1, 1, 8, 8, 9, 9, 6, 6, 2, 2, 4, 4]

# xorall = 0
# for i in arr:
#     xorall ^= i

# print(xorall)

def findUniqueOne(arr):
    n = len(arr)
    
    #Cover the corner cases:
    if n==1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    lo, hi = 1, n-2
    iterations = 0
    while lo <= hi:
        # iterations+=1
        # print(iterations, lo, hi)

        mid = (lo+hi)//2

        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        if arr[mid] == arr[mid-1]:  # second occurance
            mid = mid-1

        if mid % 2 == 0:
            lo = mid+2
        else:
            hi = mid-1


print('Final ans: ', findUniqueOne(arr))