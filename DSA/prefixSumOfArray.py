"""Problem Description
Given an array A of N integers. Construct prefix sum of the array in the given array itself."""

A = [1, 2, 3, 4, 5]
# prefix = [0]*len(A)
# prefix[0] = A[0]
# # print(prefix)
# for i in range(1, len(A)):
#     prefix[i] = prefix[i-1]+A[i]
#
# print(prefix)

for i in range(1, len(A)):
    A[i] = A[i - 1] + A[i]

print(A)
