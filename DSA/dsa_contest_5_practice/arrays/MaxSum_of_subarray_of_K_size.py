'''Given arr[ N ]. Print maximum subarray sum of subarray with length k.'''

import sys
arr = [-3, 4, -2, 5, 3, -2, 8, 2,-1, 4]

k = 5

ans, sum = -sys.maxsize, 0

# Get the prefix sum of first window.
for i in range(k):
    sum += arr[i]
ans = max(ans, sum)

# print(ans)
n = len(arr)
# Now checking for each window.
start, end = 1, k
while end <= n-1:
    sum += arr[end] - arr[start-1]
    ans = max(ans, sum)

    # print('Intermediate ans: ', ans)
    start+=1
    end +=1

print('\nFinal ans:', ans)