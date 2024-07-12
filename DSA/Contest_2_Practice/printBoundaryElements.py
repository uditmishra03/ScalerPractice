arr=[[1, 4, 2, 7],
    [3, 6, 8, 5], 
    [9, 12, 10, 13],
    [11, 14, 15, 16]]

n = len(arr)
m = len(arr[0])

for row in range(n):
    print(arr[row])

print()
i, j = 0, 0
print('Boundary elements: ')
for k in range(0, n-1):
    print(arr[i][j], end =' ')
    j+=1

for k in range(0, n-1):
    print(arr[i][j], end =' ')
    i+=1

for k in range(0, n-1):
    print(arr[i][j], end =' ')
    j-=1

for k in range(0, n-1):
    print(arr[i][j], end =' ')
    i-=1



print()