mat = [[-5, -2, 1, 13], [-4, 0, 3, 14], [-3, 2, 6, 18]]

k =0


def findelement(mat, k):
    n = len(mat)
    m = len(mat[0])

    # print(n, m)
    # set the starting point
    i , j = 0, m-1

    while i < n and j >=0:
        if mat[i][j] == k:
            return k, i, j
        if mat[i][j] > k:
            j-=1
        else:
            i+=1
        


print('mat: ')
for i in range(len(mat)):
    print(mat[i])

print('final ans(element, i, j):', findelement(mat, k))