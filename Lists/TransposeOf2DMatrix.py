# B = [[9, 8, 7],
#      [6, 5, 4],
#      [3, 2, 1]]
B= [[1,2,3], [6,7,8]]

B_transpose = []
print("Original Matrix: ")
for i in range(len(B)):
     print(B[i])

row_len = len(B)
col_len = len(B[0])

# print(row_len, col_len)
for i in range(col_len):
     row = []
     for j in range(row_len):
          row.append(B[j][i])
     B_transpose.append(row)

print("Transposed Matrix: ")
for i in range(len(B_transpose)):
     print(B_transpose[i])# row = []