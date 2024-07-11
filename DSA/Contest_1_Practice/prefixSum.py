# This is to create prefix sum of an array. Here the TC: O(N) and SC: O(N)

arr = [10, 32, 6, 12, 20, 1]

prefixSum = [0]* len(arr)
print(prefixSum)

prefixSum[0] = arr[0]
for i in range(1, len(arr)):
    prefixSum[i] = prefixSum[i-1] + arr[i]

print(prefixSum)