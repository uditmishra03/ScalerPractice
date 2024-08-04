A = [1, 2, 3, 4, 5]
B = 9


from collections import defaultdict

freq = defaultdict(int)
# mapping of sum --> index
freq[0] = -1

cur_sum , s_idx, e_idx = 0, -1 , -1

for i in range(len(A)):
    cur_sum +=A[i]
    target = cur_sum - B
    if target in freq:
        s_idx = freq[target] +1
        e_idx = i
        break
    freq[cur_sum] =i


if s_idx == -1:
    print('Not found')
    # return -1
else:
    print(A[s_idx:e_idx+1])

