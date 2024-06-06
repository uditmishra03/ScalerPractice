'''Problem Description
Give a N * N square matrix A, return an array of its anti-diagonals. Look at the example for more details.'''

arr = [[1,2,3],[4,5,6],[7,8,9]]

n = len(arr)
m = len(arr[0])
res = []


for j in range(m):
    row = 0
    col = j
    rowlist =[]
    while row < n and col >=0:
        # print(f"r:{row}, c:{col}, j: {j}")
        # print(arr[row][col], end=' ')
        rowlist.append(arr[row][col])
        row +=1
        col -=1
    k = len(rowlist)
    # print(f"k: {k}")
    while k < n:
        rowlist.append(0)
        k +=1
    # print(f" rowlist: {rowlist}", end='')
    res.append(rowlist)
    # print()
for i in range(1, n):
    row = i
    col = m-1
    rowlist = []
    while row < n and col >=0:
        # print(f"r:{row}, c:{col}")
        # print(arr[row][col], end=' ')
        rowlist.append(arr[row][col])
        row +=1
        col -=1
    k = len(rowlist)
    # print(f"k: {k}")
    while k < n:
        rowlist.append(0)
        k += 1
    res.append(rowlist)
    # print()
print(res)