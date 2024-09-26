matrix = [[10, 2, 7, 3], [9, 5, -1, 8], [3, 11, 15, 20]]

n = len(matrix)
m = len(matrix[0])

print(n, m )

ans = []

for j in range(m):
    colsum = 0
    for i in range(n):
        colsum += matrix[i][j]
    
    ans.append(colsum)

print('Final ans: ', ans)