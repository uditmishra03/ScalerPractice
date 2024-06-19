A=[[1,2,3],[4, 5,6],[7, 8,9]]

n = len(A)
m = len(A[0])

result = []
for j in range(m):
    row = 0
    col = j
    rowlist = []
    while row < n and col >= 0:
        # print(A[row][col])
        rowlist.append(A[row][col])
        row +=1
        col -=1
    # print(rowlist)
    k = len(rowlist)
    while k < n:
        rowlist.append(0)
        k +=1
    result.append(rowlist)
    # print()

for i in range(1, m):
    row = i
    col = m-1
    rowlist = []
    while row < n and col >= 0:
        # print(A[row][col])
        rowlist.append(A[row][col])
        row += 1
        col -= 1
    # print(rowlist)
    k = len(rowlist)
    while k < n:
        rowlist.append(0)
        k += 1
    result.append(rowlist)

print(result)