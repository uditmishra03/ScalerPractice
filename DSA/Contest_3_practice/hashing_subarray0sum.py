A = [1, 2, 3, 4, 5]
# A = [4, -1, 1]


def findSubarray0Sum(A):
    n = len(A)

    pf = [0]*n
    pf[0] = A[0]
    for i in range(1, n):
        pf[i] = pf[i-1] + A[i]


    print(pf)
    pf_freq ={}
    for i in pf:
        if i not in pf_freq:
            pf_freq[i] = 1
        else:
            pf_freq[i] +=1

    print(pf_freq)

    for i in pf_freq:
        if pf_freq[i] >1:
            return True
    return False


print(findSubarray0Sum(A))
