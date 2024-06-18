# mat = [[1 ,-2, -3], [-4, 5, -6], [-7, -8, 9]]
mat = [[3,2], [2, 3]]
n = len(mat)

sum = 0
for i in range(n):
    print(mat[i][i])
    sum += mat[i][i]

print("result: ", sum)