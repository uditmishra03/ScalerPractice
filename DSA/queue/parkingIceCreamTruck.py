from collections import deque
A = [1, 3, -1, -3, 5, 3, 6, 7]
B = 3

# A = [1, 2, 3, 4, 2, 7, 1, 3, 6]
# B = 6

def getMaxinSlindingWindow(A):
    dq = deque()
    ans = []

    for i in range(B):
        while len(dq) > 0 and dq[-1] < A[i]:
            dq.pop()
        dq.append(A[i])

    ans.append(dq[0])
    # print(dq)
    s, e = 1, B

    while (e < len(A)):
        if len(dq) > 0 and dq[0] == A[s-1]:
            dq.popleft()
        while len(dq) > 0 and dq[-1] < A[e]:
            dq.pop()
        dq.append(A[e])
        ans.append(dq[0])
        s+=1
        e+=1
    return ans


print('Final ans:', getMaxinSlindingWindow(A))