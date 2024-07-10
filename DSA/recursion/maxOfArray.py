'''Problem Description
Given an array A of size N, write a recursive function that returns the maximum element of the array.
'''
import sys

A = [12, 10, 3, 4, 5, 99]

def findMax(arr, cur_idx=0):
    ans = -sys.maxsize
    n = len(arr)
    if cur_idx == n:
        return ans
    ans = max(arr[cur_idx], findMax(arr, cur_idx+1))
    return ans


print(findMax(A))