
A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

# A = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]

def transpose(arr):
    n = len(arr)
    m = len(arr[0])

    transpose = []
    for i in range(m):
    
        rowlist = []
        for eachrow in arr:
            rowlist.append(eachrow[i])
            # print(eachrow[i])
        transpose.append(rowlist)
    
    return transpose


a_transpose = transpose(A)
print("Transpose of A: ", a_transpose)


for row in a_transpose:
    row.reverse()

print('Rotate matrix: ', a_transpose)