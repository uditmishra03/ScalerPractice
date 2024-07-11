'''Problem Description
Given an array of integers A and an integer B, find and return the number of pairs in A whose sum is divisible by B.

Since the answer may be large, return the answer modulo (109 + 7).

Note: Ensure to handle integer overflow when performing the calculations.'''

A = [1, 2, 3, 4, 5]
B = 2

# A = [5, 17, 100, 11]
# B = 28

n = len(A)

freq = [0]*B
# print(freq)
ans = 0

for i in range(n):
    mod_val = A[i]% B
    match = 0
    if mod_val == 0:
        match = 0
    else:
        match = B-mod_val

    print(f"for {A[i]} value of match: {match}")
    # print(freq)

    count = freq[match]
    print(count, freq[match])
    ans += count
    freq[mod_val] +=1


print(freq)
print(ans)
