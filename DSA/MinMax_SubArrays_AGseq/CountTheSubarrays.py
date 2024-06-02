'''Problem Description
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.'''

A = [2, 5, 6]
B = 10

n = len(A)

def prefixsum(arr):
    print('original array: ', arr)
    pf = [0]*len(arr)
    pf[0] = arr[0]
    # print(pf)
    for k in range(1, len(arr)):
        # print(k, pf[k-1])
        pf[k] = pf[k-1] + arr[k]
    return pf

# results =[]
count = 0
for i in range(n):
    for j in range(i+1, n+1):
        # print(A[i:j])
        tmparr = A[i:j]
        pf_tmparr = prefixsum(tmparr)
        print('pf: ',pf_tmparr, pf_tmparr[-1])

        if pf_tmparr[-1] < B:
            count +=1

print(count)