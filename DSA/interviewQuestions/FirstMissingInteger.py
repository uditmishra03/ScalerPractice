'''Problem Description
Given an unsorted integer array, A of size N. Find the first missing positive integer.

Note: Your algorithm should run in O(n) time and use constant space.

'''

# arr = [1, 2, 0]
# arr = [2,3,1,2]
arr = [3, 4, -1, 1]
# arr = [-8, -7, -6]
n = len(arr)
# print(n, n+2)

def findmissingelement(arr):
    for i in range(n):
        if arr[i] <= 0:
            arr[i] = n+2

    print(arr)

    for i in range(n):
        ele = abs(arr[i])
        idx = ele -1
        if idx >= 0 and idx < n and arr[idx]>0:
            arr[idx] *= -1
            print(arr)
    # print(arr)
    # ans =
    for i in range(n):
        if arr[i] > 0:
            return i+1
    return n+1
    # print(arr)
    # print(n+1)

print(findmissingelement(arr))