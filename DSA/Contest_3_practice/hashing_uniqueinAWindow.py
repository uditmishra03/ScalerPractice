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
print('First window:', freq)
# print(ans)

print()
n = len(A)
start , end = 1, B

while end < n:
    freq[A[end]] +=1
    freq[A[start-1]] -=1

    if freq[A[start-1]] == 0:
        print('popping ', A[start-1])
        freq.pop(A[start-1])

    print('Updated freq ', freq)
    ans.append(len(freq))

    start +=1
    end +=1

    print()

print('Final ans: ', ans )



