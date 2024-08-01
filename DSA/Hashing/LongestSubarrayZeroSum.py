
from collections import defaultdict

# A = [1, -2, 1, 2]
A = [9,-20,-11,-8,-4,2,-12,14,1]
# A = [3, 2, -1]

n = len(A)
freq = defaultdict(int)

max_len , cur_sum = 0, 0

for i in range(n):
    cur_sum += A[i]

    if cur_sum == 0:
        max_len = i+1
    
    if cur_sum in freq:
        max_len = max(max_len, i-freq[cur_sum])  # Getting the subarray length from the 
                                                #previous prefix sum we found.
    else:
        freq[cur_sum]= i # storing the index of each sum as it value

    # print(max_len)
    
print('final ans: ', max_len)

