'''Problem Description
Given 2 integers A and B and an array of integers C of size N. Element C[i] represents the length of ith board.
You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of the board.

Calculate and return the minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of the board.
NOTE:
1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. This means a configuration where painter 1 paints boards 1 and 3 but not 2 is invalid.

Return the ans % 10000003.'''

def check(arr, mid, k, t):
    n = len(arr)
    cur_sum = 0
    num_painters = 1
    for i in range(n):
        if cur_sum + arr[i]*t <= mid:
            cur_sum += arr[i]*t
        else:
            num_painters +=1
            cur_sum = arr[i]*t
    if num_painters <= k:
        return True
    else: 
        return False


def paint(A, B, C):

    n = len(C)
    sumOfC = 0
    for i in range(n):
        sumOfC += C[i]
    ans = 0
    lo, hi = max(C)*B, sumOfC*B

    while lo <= hi:
        mid = (lo+hi)//2
        if check(C, mid, A, B) == True:
            ans = mid
            hi = mid-1
        else:
            lo = mid+1
    
    return ans % 10000003


# A = 2
# B = 5
# C = [1, 10]

A = 10
B = 1
C = [1, 8, 11, 3]
print('Final ans:', paint(A, B, C))