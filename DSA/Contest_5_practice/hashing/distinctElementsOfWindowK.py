from collections import defaultdict

# A = [1, 2, 1, 3, 4, 3]
# B = 3

A = [1, 1, 2, 2]
B = 1

freq = defaultdict(int)

ans = []

for i in range(B):
    freq[A[i]] +=1

ans.append(len(freq))

# print(freq)
print(ans)

start, end = 1, B
while end < len(A):
    freq[A[start-1]] -=1
    freq[A[end]] +=1

    if freq[A[start-1]] == 0:
        freq.pop(A[start-1])

    ans.append(len(freq))
    start +=1
    end +=1

print('Final ans:', ans)