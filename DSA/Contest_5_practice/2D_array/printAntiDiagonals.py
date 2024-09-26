arr = [[1,2,3],[4,5,6],[7,8,9]]

# arr = [[1,2,3,4,5], [6, 7,8, 9,10], [11,12,13,14,15], [16,17,18, 19, 20]]

n = len(arr)
m = len(arr[0])

antidiagonals = []

for j in range(m):
    row = 0
    col = j
    rowlist=[]
    while row < n and col >= 0:
        rowlist.append(arr[row][col])
        row +=1
        col -=1

    k = len(rowlist)
    while k<n:
        rowlist.append(0)
        k+=1
    antidiagonals.append(rowlist)

for i in range(1, n):
    row , col = i, m-1
    rowlist=[]
    while row < n and col >= 0:
        rowlist.append(arr[row][col])
        row +=1
        col -=1

    k = len(rowlist)
    while k<n:
        rowlist.append(0)
        k+=1
    antidiagonals.append(rowlist)

print(antidiagonals)