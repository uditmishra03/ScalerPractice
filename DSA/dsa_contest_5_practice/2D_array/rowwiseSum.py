matrix = [[10, 2, 7, 3], [9, 5, -1, 8], [3, 11, 15, 20]]

n = len(matrix)
m = len(matrix[0])

print(n, m )

ans = []
for i in range(n):
    rowsum=0
    for j in range(m):
        rowsum +=matrix[i][j]
    ans.append(rowsum)



print("Final ans: ", ans)
