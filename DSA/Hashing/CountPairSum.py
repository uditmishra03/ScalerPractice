'''You are given an array A of N integers and an integer B. Count the number of pairs (i,j) such that A[i] + A[j] = B and i ≠ j.

Since the answer can be very large, return the remainder after dividing the count with 109+7.

Note - The pair (i,j) is same as the pair (j,i) and we need to count it only once.'''

from collections import defaultdict


# A = [3, 5, 1, 2]
# B = 8

A = [1, 2, 1, 2]
B = 3

def countPairSum(A, B):
    n = len(A)
    freq = defaultdict(int)
    count = 0

    for i in range(n):
        target = B-A[i]
        if target in freq:
            count += freq[target]
        
        freq[A[i]] +=1
    
    return count

print('final ans: ', countPairSum(A, B) )
