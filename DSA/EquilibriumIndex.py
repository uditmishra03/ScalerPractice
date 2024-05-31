"""Problem Description
You are given an array A of integers of size N.

Your task is to find the equilibrium index of the given array

The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.

If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.

Note:

Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index."""

A = [-7, 1, 5, 2, -4, 3, 0]

def prefixSum(arr):
    prefixSum = [0]*len(arr)
    prefixSum[0] = arr[0]
    for i in range(len(arr)):
        prefixSum[i] = prefixSum[i-1]+arr[i]
    return prefixSum

pf = prefixSum(A)

# def sumOfArray(arr):
#     sum = 0
#     for i in arr:
#         sum += i
#     return sum
# sum = sumOfArray(A)

def suffixSum(A):
    # print(A)
    # n = len(A)
    suffixSum = [0]*len(A)
    suffixSum[-1] = A[-1]
    for i in range(len(A)-2, -1, -1):
        # print(i, i-1)
        suffixSum[i] = suffixSum[i+1]+A[i]

    return suffixSum


def equiIndex(A):
    sf = suffixSum(A)
    pf = prefixSum(A)
    # print(pf)
    # print(sf)
    equilibriumIndex , index = False, 0
    for i in range(len(A)):
        # print(sf[i], pf[i])
        if sf[i] == pf[i]:
            equilibriumIndex = True
            index = i
            break

    if equilibriumIndex:
        return index
    else:
        return -1

print(equiIndex(A))