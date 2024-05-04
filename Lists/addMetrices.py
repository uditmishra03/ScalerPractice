A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

# print(len(A[0]))
# print(B)
C = []
#
for i in range(len(A)):
     c_row = []
     for j in range(len(A[i])):
          c_row.append(A[i][j] + B[i][j])
     C.append(c_row)

print('Result:')
# print(len(A))
for i in range(len(C)):
     print(C[i])
     for j in range(len(C[i])):
          print(i, j, C[i][j])

# print(C)