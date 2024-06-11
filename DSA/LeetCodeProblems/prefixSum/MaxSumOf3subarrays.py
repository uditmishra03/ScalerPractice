'''Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.'''

nums = [1,2,1,2,6,7,5,1]
k = 2
n = len(nums)
pfsum = [0]*n
pfsum[0] = nums[0]
for i in range(1, n):
    pfsum[i] = pfsum[i-1] + nums[i]

print(pfsum)
ans = 0
start = 0
end = k-1
print(pfsum[start-1])
# while end <= n-1:
#     sum = pfsum[end] - pfsum[start-1]
#     # print(sum)
#     ans = max(ans, sum)
#
# print(ans)

while end <= n:
    print(nums[start:end+1])
    start +=2
    end +=2