'''You are given a sorted array A of size N and a target value B.
Your task is to find the index (0-based indexing) of the target value in the array.

If the target value is present, return its index.
If the target value is not found, return the index of least element greater than equal to B.
If the target value is not found and least number greater than equal to target is also not present, return the length of array (i.e. the position where target can be placed)'''

# A = [1, 3, 5, 6]
# B = 5 

A = [1, 4, 9]
B = 5

def searchAndInsert(arr, k):
    n = len(arr)
    lo, hi = 0, n-1
    ans = n
    while lo <= hi:
        mid = (lo+hi)//2
        if arr[mid] == k:
            # ans = mid
            return mid
        elif arr[mid] <k:
            lo = mid+1
        else:
            hi = mid-1
        print(lo, hi)
    return hi+1

print('final ans:', searchAndInsert(A, B))
    
