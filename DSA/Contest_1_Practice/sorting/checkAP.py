A = [3, 5, 1]
# A = [2, 4, 1]



def checkAp(A):
    A.sort()
    # print(A)

    diff = A[1] - A[0]
    # print(diff)

    for i in range(1, len(A)):
        # print(A[i] - A[i-1])
        if diff != (A[i] - A[i-1]):
            return 0

    return 1
print(checkAp(A))