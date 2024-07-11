A=[[1,2,3],[4, 5,6],[7, 8,9]]

n = len(A)
m = len(A[0])
print('n', n,'m',  m)
res = []

for j in range(m):
    row = 0
    col = j
    rowlist =[]
    while row < n and col >=0:
        rowlist.append(A[row][col])
        row +=1
        col -=1
    # print(f"len: ",len(rowlist))
    k = len(rowlist)
    while k < n:
        rowlist.append(0)
        k +=1
    # print(rowlist)
    res.append(rowlist)

for i in range(1, n):
    row = i         # rOW CHANGES SO i.
    col = m-1       # Col does not changes
    rowlist = []
    while row < n and col >= 0:
        # print(A[row][col])
        rowlist.append(A[row][col])
        row += 1
        col -= 1
    # print(f"len: ", len(rowlist))
    k = len(rowlist)
    while k < n:
        rowlist.append(0)
        k += 1
    # print(rowlist)
    res.append(rowlist)

# print(res)
for i in range(len(res)):
    for j in range(len(res[0])):
        print(res[i][j], end =' ')
    print()