from collections import defaultdict

A = [1, 2, 3, 4, 5]
B = 5

# A = [5, 10, 20, 100, 105]
# B = 110

def SubarraySum(A, B): 
    n = len(A)

    hash = defaultdict(int)
    hash[0]= -1
    # print(hash)

    cur_sum =0
    start_idx, end_idx = -1, -1
    # ans = []
    for i in range(n):
        cur_sum += A[i]
        target = cur_sum - B
        if target in hash:
            start_idx = hash[target] +1
            end_idx = i
            break
        hash[cur_sum] =i
        # print(hash)

    if start_idx == -1:
        return [-1]

    else:
        return A[start_idx:end_idx+1]

# print(start_idx, end_idx)
print(SubarraySum(A, B))

