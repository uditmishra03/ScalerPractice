'''Given an integer array A of size N. You can remove any element from the array in one operation.
The cost of this operation is the sum of all elements in the array present before this operation.
Find the minimum cost to remove all elements from the array.'''

A = [2, 1]
# A = [5]

# 1. sort the array
A.sort()
# print(A)
# reverse the array
A.reverse()
# print(A)

ans = 0
for i in range(len(A)):
    # print(i, A[i])
    ans += (i+1)* A[i]
print(ans)