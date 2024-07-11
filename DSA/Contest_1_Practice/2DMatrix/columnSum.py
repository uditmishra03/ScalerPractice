a= [[1,2,3,4], [5,6,7,8], [9,2,3,4] ]

n = len(a)
m = len(a[0])
# print(n, m, a[0])
result =[]
for j in range(m):
    # print('row', i, ':', a[i])
    sum = 0
    for i in range(n):
        print(a[i][j], end =', ')
        sum += a[i][j]
    result.append(sum )
    print()

print(result)