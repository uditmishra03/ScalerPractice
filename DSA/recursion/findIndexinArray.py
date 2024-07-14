'''
Problem Description
You are given an array A of size N. Write a recursive function that returns the first index at which an integer B is found in the array.'''

A = [-3, 5, 6, 2]  
B = 6

A = [0, 1, 0, 2]  
B = 3


def findIndex(arr, b, cur_idx =0):
    n = len(arr)
    if cur_idx == n:
        return -1
    if arr[cur_idx] == b:
        return cur_idx
    else:
        return findIndex(arr, b, cur_idx+1)



ans = findIndex(A, B)
print(ans)