'''Problem Description
You are given an array A of integers of size N.
Your task is to find the equilibrium index of the given array
The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes.
If there are no elements that are at lower indexes or at higher indexes, then the corresponding sum of elements is considered as 0.
Note:
Array indexing starts from 0.
If there is no equilibrium index then return -1.
If there are more than one equilibrium indexes then return the minimum index.'''

# A = [-7, 1, 5, 2, -4, 3, 0]
A = [1, 2, 3]
n = len(A)
# Create prefix sum
prefixSum = [0] * n
prefixSum[0] = A[0]
for i in range(1, n):
    prefixSum[i] = prefixSum[i - 1] + A[i]

# create suffix sum
suffixSum = [0] * n
suffixSum[-1] = A[-1]
for i in range(n - 2, -1, -1):
    suffixSum[i] = suffixSum[i + 1] + A[i]

print(prefixSum, suffixSum, sep='\n')
equilibriumIndex = False
for i in range(n):
    if prefixSum[i] == suffixSum[i]:
        index = i
        equilibriumIndex = True
        break
if equilibriumIndex:
    print(f"1, equilibrium index: {index}")
else:
    print(f" -1, equilibrium index not found")

# Run a loop on both suffix and prefix sum, and check values for each index,
# if value are equal, return the equilibrium index.