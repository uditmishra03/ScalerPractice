A= [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]

n = len(A)
m = len(A[0])


for row in range(n):
    print(A[row])

print()
i, j = 0, 0
print('Spiral matrix elements: ')
while n > 1:
    
    for k in range(0, n-1):
        print(A[i][j], end =' ')
        j+=1

    for k in range(0, n-1):
        print(A[i][j], end =' ')
        i+=1

    for k in range(0, n-1):
        print(A[i][j], end =' ')
        j-=1

    for k in range(0, n-1):
        print(A[i][j], end =' ')
        i-=1
    
    # print("\n", n, i, j)

    i +=1
    j +=1
    n -=2

if n ==1:
    print(A[i][j])

print()