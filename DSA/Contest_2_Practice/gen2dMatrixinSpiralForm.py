def print2DMat(mat):
    for i in range(len(mat[0])):
        print(mat[i])


n =3

mat = [row[:] for row in [[0]*n]*n]
print('Original matrix: ', mat)

# print(mat)
value = 1
i, j = 0, 0
print('Spiral matrix elements: ')
while n > 1:
    for k in range(n-1):
        mat[i][j] = value
        value +=1
        j+=1
    
    print(print2DMat(mat))
    print(i, j , value)
    for k in range(n-1):
        mat[i][j] = value
        value +=1
        i+=1
    print(print2DMat(mat))
    for k in range(n-1):
        mat[i][j] = value
        value +=1
        j-=1
    print(print2DMat(mat))
    for k in range(n-1):
        mat[i][j] = value
        value +=1
        i-=1
    print(print2DMat(mat))
    # print("\n", n, i, j)

    i +=1
    j +=1
    n -=2

if n == 1:
    mat[i][j]= value
    # value +=1


print(mat)