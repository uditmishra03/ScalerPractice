from collections import defaultdict


arr = [2, 3, -5, 7, -2, 1, -6, 4, 1]

mod = (10**9+7)
n = len(arr)
pfsum = [0]*n
pfsum[0] = arr[0]

for i in range(1, n):
    pfsum[i] = pfsum[i-1]+arr[i]

print(pfsum)

count = 0
freq = defaultdict(int)

freq[0] = 1
for i in pfsum:
    if i not in freq:
        freq[i] =1
    else:
        count += freq[i]
        freq[i] +=1

print('Final count: ', count%mod)