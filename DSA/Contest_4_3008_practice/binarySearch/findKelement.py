arr = [3, 6, 9, 12, 14,	19,	20,	23,	25, 27]

print(arr)

def findKelement(arr, k):
    n = len(arr)

    lo = 0
    hi = n
    count = 0
    while lo <= hi:
        count +=1
        mid = (lo+hi)//2
        if arr[mid] == k:
            return mid, count
        elif arr[mid] < k:
            lo = mid+1
        else:
            hi = mid-1
    # print(count)
    return -1, count


print('Final ans:', findKelement(arr, 23))

print('Final ans:', findKelement(arr, 15))
print('Final ans:', findKelement(arr, 3))