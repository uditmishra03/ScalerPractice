# Problem Description
# Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
# and at least one occurrence of the minimum value of the array.
import sys

A= [2,2,6,4,5,1,5,2,6,4,1]
# A = [2, 6, 1, 6, 9]
# A = [1, 3, 2]
# 1. find the min and max values of array.
# 2. set the mix_idx and max_idx as -1 each,
# set the ans = sys.maxsize
# 3. Traverse the array and find the index of min and max value of array.array
# 4. Now if the min and max idx are valid only then find the min of (ans and subarray len = right - left+1)

min_val, max_val = min(A), max(A)
min_idx, max_idx = -1, -1

print(min_val, max_val)

ans = sys.maxsize

for i in range(len(A)):
    if A[i] == min_val:
        min_idx = i
    elif A[i] == max_val:
        max_idx = i

print(f"@{min_idx}: {A[min_idx]},@{max_idx}: {A[max_idx]}")

if min_idx != -1 and max_idx != -1:
    subarray_len = abs(max_idx-min_idx)+1
    # print(subarray_len)
    ans = min(ans, subarray_len)

print(ans)
if min_idx < max_idx:
    print(A[min_idx:max_idx+1])
else:
    print(A[max_idx:min_idx + 1])