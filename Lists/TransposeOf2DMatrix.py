B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]

B_transpose = []
print("Original Matrix: ")
for i in range(len(B)):
     print(B[i])
for i in range(len(B)):
     row = []
     for j in range(len(B[i])):
          row.append(B[j][i])
     B_transpose.append(row)

# print(B_transpose)
print("Transposed Matrix: ")
for i in range(len(B_transpose)):
     print(B_transpose[i])# row = []
     # for j in range(len(B_transpose[i])):
     #      print(B_transpose[i][j])