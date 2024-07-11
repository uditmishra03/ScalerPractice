# A = [3, 7, 90, 20, 10, 50, 40]
# B = 3
A = [3, 7, 5, 20, -10, 0, 12]
B = 2
sum = 0
for i in range(B):
    sum += A[i]
startingIndex = 0
ans = sum

print('Answer so far in 1st run: ', ans, 'Starting Index: ', startingIndex)

start =1
end = B
# print(A[start:end+1])
while end < len(A):
    # print(A[end])
    sum += A[end] - A[start-1]
    # print('sum: ', sum)
    if ans > sum:
        startingIndex = start
        ans = sum
    end +=1
    start +=1
print('Answer: ', ans, 'Starting Index: ', startingIndex, 'window: ', A[startingIndex: startingIndex+B])
