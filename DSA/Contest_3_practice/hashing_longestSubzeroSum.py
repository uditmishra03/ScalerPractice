# A = [1, -2, 1, 2]
A = [9,-20,-11,-8,-4,2,-12,14,1]
# A = [3, 2, -1]


from collections import defaultdict

freq = defaultdict(int)

max_len, cur_sum = 0, 0

for i in range(len(A)):
    cur_sum +=A[i]

    if cur_sum == 0:
        max_len = i+1

    if cur_sum in freq:
        # print(freq[cur_sum], i)
        max_len = max(max_len, i-freq[cur_sum])
    else:
        freq[cur_sum] =i

print('final ans:',  max_len)