from collections import defaultdict

A = [1, 2, 3, 4, 5]
B = 10

start_idx , end_idx = -1, -1
freq = defaultdict(int)
cur_sum = 0
freq[0]= 0

for i in range(len(A)):
    cur_sum +=A[i]
    target = cur_sum - B

    if target ==0:
        start_idx = 0
        end_idx = i
        break

    if target in freq:
        start_idx = freq[target] +1
        end_idx = i
        break
    freq[cur_sum] = i

if start_idx == -1:
    print('Not found. -1')
else:
    print('Found it: ', A[start_idx: end_idx+1])