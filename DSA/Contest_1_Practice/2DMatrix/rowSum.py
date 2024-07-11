A= [[1,2,3,4],
[5,6,7,8],
[9,2,3,4]]

n = len(A)
m = len(A[0])

results = []
for i in range(n):
    sum = 0
    for j in range(m):
        print(A[i][j], end =' ')
        sum += A[i][j]
    results.append(sum)
    print()

print(results)

colSum_res=[]
for i in range(m):
    colSum =0
    for j in range(n):
        print(A[j][i], end = ' ')
        colSum += A[j][i]
    colSum_res.append(colSum)
    print()

print(colSum_res)
