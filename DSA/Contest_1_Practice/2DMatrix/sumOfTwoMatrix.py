# A = [[1, 2, 3],
#      [4, 5, 6],
#      [7, 8, 9]]
#
# B = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]

A = [[1, 2, 3],
     [4, 1, 2],
     [7, 8, 9]]

B = [[9, 9, 7],
     [1, 2, 4],
     [4, 6, 3]]

n = len(A)
m = len(A[0])

resultant = []

for i in range(n):
    row= []
    for j in range(m):
        row.append(A[i][j]+B[i][j])
    resultant.append(row)

print(resultant)