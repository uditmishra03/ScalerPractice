'''Problem Description
You are given an integer array A of length N.
You are also given a 2D integer array B with dimensions M x 2, where each row denotes a [L, R] query.
For each query, you have to find the sum of all elements from L to R indices in A (0 - indexed).
More formally, find A[L] + A[L + 1] + A[L + 2] +... + A[R - 1] + A[R] for each query.'''

A = [1, 2, 3, 4, 5]
B = [[0, 3], [1, 2], [0, 4]]

# A = [2, 2, 2]
# B = [[0, 0], [1, 2]]

n = len(A)
results = []
prefixsum = [0]*n
prefixsum[0] = A[0]
for i in range(1, n):
    prefixsum[i] = prefixsum[i-1]+A[i]
print(prefixsum)

for each in B:
    # print(each)
    L, R = each[0], each[1]
    if L == 0:
        # print(prefixsum[R], prefixsum[L - 1])
        rangesum = prefixsum[R]
    else:
        # print(prefixsum[R], prefixsum[L - 1])
        rangesum = prefixsum[R] - prefixsum[L - 1]
    results.append(rangesum)
    print(f"for L:{L}, R:{R}, rangesum:{rangesum}")
    # print(rangesum)
print(results)