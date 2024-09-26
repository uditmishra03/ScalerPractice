A = [[1, 2, 3, 4], 
     [12, 13, 14, 5],
     [11, 16, 15, 6],
     [10, 9, 8, 7]]


def printBoundaryElements(arr):
    n = len(arr)
    boundaryElements = []

    i, j = 0, 0
    for k in range(n-1):
        # print(arr[i][j])
        boundaryElements.append(arr[i][j])
        j+=1
    for k in range(n-1):
        # print(arr[i][j])
        boundaryElements.append(arr[i][j])
        i+=1
    for k in range(n-1):
        # print(arr[i][j])
        boundaryElements.append(arr[i][j])
        j-=1
    for k in range(n-1):
        # print(arr[i][j])
        boundaryElements.append(arr[i][j])
        i-=1
    return boundaryElements

print(printBoundaryElements(A))

# i , j =0, 0

# n = len(A)
# while n > 1:
    
#     i+=1
#     j +=1
#     n -=2
