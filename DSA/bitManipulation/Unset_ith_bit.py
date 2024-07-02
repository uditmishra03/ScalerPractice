'''Problem Description
You are given two integers A and B.
If B-th bit in A is set, make it unset.
If B-th bit in A is unset, leave as it is.
Return the updated A value.'''

A = 5
B = 2

# bin_A = bin(A)[2:]
# print(bin_A, type(bin_A))
#
# # for each in bin_A:
# #     print(each)
#
# print(bin_A and 1 << B)

def unSetithBit(A, B):
    if A & 1 <<B != 0:
        A = A ^ 1 << B
    return A

print(unSetithBit(4, 1))