A = [[1, -2, -3],
     [-4, 5, -6],
     [-7, -8, 9]]
A = [[3, 2],
     [2, 3]]
# A = [[2,3,6,7],[2,3,4,5]]
n = len(A)
# m = len(A[0])

row = 0
col = n-1
sum = 0
while row < n and col >= 0:
     print(A[row][col])
     sum += A[row][col]
     row +=1
     col -=1

print('result: ', sum)