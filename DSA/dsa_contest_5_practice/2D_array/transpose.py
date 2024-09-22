A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

n = len(A)
m = len(A[0])

result = []
for i in range(m):
    rowlist = []
    for eachrow in A:
        rowlist.append(eachrow[i])
        # print(eachrow[i])
    result.append(rowlist)
    # print()

print(result)