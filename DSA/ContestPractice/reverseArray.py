'''Problem Description
Given an array A of N integers and also given two integers B and C. Reverse the elements of the array A within the given inclusive range [B, C].'''

A = [2, 5, 6, 9, 3, 12, 45, 23, 45, 265, 82]
B = 4
C = 10
# A = [1, 2, 3, 4]
# B = 2
# C = 3
n = len(A)

while B < C:
    print(B, C)
    A[B], A[C] = A[C], A[B]
    B += 1
    C -= 1

print(A)
