from collections import deque


# A = [2, 5, -1, 7, -3, -1, -2]
# B = 4

A = [2, -1, 3]
B = 2

def getMaxinSlindingWindow(A, B):
    dq = deque()
    max_ans = []

    for i in range(B):
        while len(dq) > 0 and dq[-1] < A[i]:
            dq.pop()
        dq.append(A[i])

    max_ans.append(dq[0])
    # print(dq)
    s, e = 1, B

    while (e < len(A)):
        if len(dq) > 0 and dq[0] == A[s-1]:
            dq.popleft()
        while len(dq) > 0 and dq[-1] < A[e]:
            dq.pop()
        dq.append(A[e])
        max_ans.append(dq[0])
        s+=1
        e+=1
    return max_ans

def getMininSlindingWindow(A, B):
    dq = deque()
    min_ans = []

    for i in range(B):
        while len(dq) > 0 and dq[-1] > A[i]:
            dq.pop()
        dq.append(A[i])

    min_ans.append(dq[0])
    # print(dq)
    s, e = 1, B

    while (e < len(A)):
        if len(dq) > 0 and dq[0] == A[s-1]:
            dq.popleft()
        while len(dq) > 0 and dq[-1] > A[e]:
            dq.pop()
        dq.append(A[e])
        min_ans.append(dq[0])
        s+=1
        e+=1
    return min_ans

max_ans = getMaxinSlindingWindow(A, B)
min_ans = getMininSlindingWindow(A, B)

# print(max_ans)
# print(min_ans)
sum = 0
for i in range(len(max_ans)):
    sum += max_ans[i] + min_ans[i]

print('Final ans:', sum)
