A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
B = 2

n = len(A)
m = len(A[0])

for i in range(n):
    for j in range(m):
        A[i][j] = A[i][j] * B
print(A)
