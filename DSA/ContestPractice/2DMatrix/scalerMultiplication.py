# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
# B = 2

A = [[1]]
B = 5

n = len(A)
m = len(A[0])

resultant= []

for i in range(n):
    rowlist= []
    for j in range(m):
        rowlist.append(A[i][j]*B)
    resultant.append(rowlist)

print(resultant)
