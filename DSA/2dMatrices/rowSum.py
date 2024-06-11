'''Input Format
First argument A is a 2D array of integers.(2D matrix).'''

A= [[1,2,3,4],
[5,6,7,8],
[9,2,3,4]]

results = []
for i in range(len(A)):
    sum = 0
    for j in range(len(A[0])):
        # print(A[i][j], end=' ')
        sum += A[i][j]
    results.append(sum)

print(results)