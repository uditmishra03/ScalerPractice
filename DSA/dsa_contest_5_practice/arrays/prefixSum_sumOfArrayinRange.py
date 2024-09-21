A = [3, -2, 8, -5, 4, 0, 1]


def prefixSum(arr):
    n = len(arr)

    pfsum = [0]*n

    pfsum[0] = arr[0]

    for i in range(1, n):
        pfsum[i] = pfsum[i-1] + arr[i]

    return pfsum


pf = prefixSum(A)
print("pfsum of\noriginal array:\t", A, "\nis:\t\t", prefixSum(A))


range= [[0, 2], [3, 6], [0, 6], [2, 5]]
print('Find the sum of array withing range: ', range)

for each in range:
    l, r = each[0], each[1]

    print(l, r)
    if l == 0:
        print("sum of array for range: ", each, "is: ", pf[r])
    else:
        print("sum of array for range: ", each, "is: ", pf[r]- pf[l-1])

