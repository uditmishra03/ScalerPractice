from collections import defaultdict

# A = [1, -2, 1, 2]
A = [1, 3, 0, -3, 4, -1]

n = len(A)
freq = defaultdict(int)

max_len , cur_sum = 0, 0

# pfsum = [0]*n
# pfsum[0] = A[0]
# for i in range(1, n):
#     pfsum[i] = pfsum[i-1] + A[i]

# # print(pfsum)
# cur_sum = 0
for i in range(n):
    cur_sum += A[i]
    if cur_sum == 0:
        max_len = i+1
    if cur_sum in freq:
        max_len = max(max_len, i-freq[cur_sum])
    else:
        freq[cur_sum] = i

print(freq)
print('Final ans:', max_len)