A=  [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
 ]

print('Original Matrix: ', A)
n = len(A)

#1. get the transpose of matrix,
result = []
for j in range(n):
    row = []
    for i in range(n):
        row.append(A[i][j])
    result.append(row)

print('Transposed Mat:', result)

# reverse each row of previous result.
# result = []
for i in result:
    i.reverse()
    # print(i.reverse())

print('Result: ', result)


