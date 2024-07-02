'''Problem Description
You are given two integers A and B.
Set the A-th bit and B-th bit in 0, and return output in decimal Number System.'''

# A, B = 3, 5

A, B = 4, 4

print(2^A, 2^B)
if A == B:
    ans = 0 + 0^1 << A
else:
    ans = 0 + 0^1 << A + 0^1 << B

print('ans:', ans)