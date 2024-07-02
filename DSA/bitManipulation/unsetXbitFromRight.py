'''Problem Description
Given an integer A. Unset B bits from the right of A in binary.

For example, if A = 93 and B = 4, the binary representation of A is 1011101.
If we unset the rightmost 4 bits, we get the binary number 1010000, which is equal to the decimal value 80.'''

# A = 93
# B = 4

A = 37
B = 3
ans =0
for i in range(B):
    if A & 1 << i !=0:
        A = A ^ 1 << i
print(A)
