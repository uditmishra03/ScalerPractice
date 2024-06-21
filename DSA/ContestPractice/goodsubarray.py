A = [1, 2, 3, 4, 5]

n = len(A)

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += A[j]
        print(A[i:j])
    print('sum:', sum)
    print()
        # print(A[i:j])