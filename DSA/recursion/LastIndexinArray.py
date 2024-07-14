"""Problem Description
You are given an array A of size N. Write a recursive function that returns the last index at which an integer B is found in the array.

NOTE: If B is not found anywhere in the array then return -1."""

A = [6, 5,6, 2]  
B = 6


def findLastIndex(arr, b, cur_idx):
    n = len(arr)
    if cur_idx==-1:
        return -1
    if arr[cur_idx]==b:
        return cur_idx
    else:
        return findLastIndex(arr, b, cur_idx-1)
    


n = len(A)
print(findLastIndex(A, B, n-1))
# ans = findLastIndex(A, B, n-1)

# print(ans)