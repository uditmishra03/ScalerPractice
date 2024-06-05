'''Problem Description
Given an array A of size N, find the subarray of size B with the least average.'''

A = [3, 7, 90, 20, 10, 50, 40]
B = 3
k = B
# start = 0
# end = k
sum = 0
print(A)
for i in range(0, k):
    sum = sum + A[i]
# minavg = round(sum/k, 2)
ans_sum = sum
start = 1
end = k
index = 0
while end < len(A):
    sum = sum +A[end] - A[start-1]
    if ans_sum > sum:
        ans_sum = sum
        # print(sum, start, end)
        index = start
    start +=1
    end +=1

print(ans_sum, ans_sum/k, index)