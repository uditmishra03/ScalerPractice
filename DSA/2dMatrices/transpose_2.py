# from transpose import print2Darray

# A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
A = [[1, 2],[1, 2],[1, 2]]

print(A)
n = len(A)
m = len(A[0])
res = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(A[j][i])
    # print(f"row: {row}")
    res.append(row)
print(res)