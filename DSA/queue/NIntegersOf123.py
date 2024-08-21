'''Problem Description
Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.

NOTE: All the A integers will fit in 32-bit integers.'''

from collections import deque

# A = 3
A = 7

s = ["" for i in range(0, 29500)]
s[0] = "1"
s[1] = "2"
s[2] = "3"
q = deque()
q.append(s[0])
q.append(s[1])
q.append(s[2])

# print(q)

ans = []
idx = 3
while idx < A:
    ss = q.popleft()
    ans.append(ss)
    s[idx] = ss + "1"
    idx = idx + 1
    q.append(ss + "1")

    s[idx] = ss + "2"
    idx = idx + 1
    q.append(ss + "2")

    s[idx] = ss + "3"
    idx = idx + 1
    q.append(ss + "3")


# print("ans:", ans)

while len(ans) < A:
    ans.append(q.popleft())

print("ans:", ans, 'size:', len(ans))