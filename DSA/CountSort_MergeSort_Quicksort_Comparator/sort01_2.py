A = [0,0,1,0,1,1,0]
# A = [1,0]



n = len(A)
i, j = 0, n - 1
while i < j:
    print(f'values of i: {i}, and j: {j}')
    if A[i] == 1:
        A[i], A[j] = A[j], A[i]
        j -= 1
    else:
        i += 1

print(A)