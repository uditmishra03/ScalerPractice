A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

n = len(A)
m = len(A[0])

for i in range(n):
    for j in range(m):
        # print(i, j,sep= ',', end = ' ')
        print(A[i][j], end =' ')
    print()


print('Transpose:')
transpose = []
for i in range(m):
    row = []
    for j in range(n):
        print(A[j][i], end=' ')
        row.append(A[j][i])
        # print(j, i,sep= ',', end = ' ')
    transpose.append(row)
    print()

print(transpose)

