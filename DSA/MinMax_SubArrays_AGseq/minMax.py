"""Problem Description
Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array

and at least one occurrence of the minimum value of the array"""

# Input 1:
import sys

'''# find/define max_val and min_val from the array
# 2. Init latest_max, latest_min as -1 each
# 3. set your ans i.e., the lenght of subarrya as maxsize of integer can have, 64 bit.
# 4. Run a loop from 0 till n-1
4a. if arr[i] == min_val , then set the latest_min as i (index)
4b. if arr[i] == max_val , then set the latest_max as i (index)
4c. check if latest_max and latest_min both are != -1
 if yes then find the min( ans, abs(latest_max - latest_min) +1) as your ans.
 5. return ans.'''


# A = [1, 3, 2]
# Input 2:
arr = [2, 6, 1, 6, 9]
# A = [2, 2, 6, 4, 5, 1,5, 2, 6,4, 1]

def MinMax(A):
    min_val, max_val = min(A), max(A)
    print(min_val, max_val)

    latest_min, latest_max = -1, -1
    ans = sys.maxsize

    for i in range(len(A)):
        if A[i] == min_val:
            latest_min = i
        if A[i] == max_val:
            latest_max = i

        if latest_min != -1 and latest_max != -1:
            ans = min(ans, abs(latest_max - latest_min) +1)

    print(ans, "| min: ", latest_min, "max: ", latest_max)
    if latest_min < latest_max:
        print(A[latest_min: latest_max + 1])
    else:
        print(A[latest_max: latest_min+1])


MinMax(arr)