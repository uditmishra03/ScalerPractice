
A = [[1, 3], [6, 9]]
B = [2, 5]
ans = []
i, n = 0, len(A)

while i < n and A[i][1] <= B[0]:
    ans.append(A[i])
    i += 1

while i < n and A[i][0] <= B[1]:
    B[0] = min(B[0], A[i][0])
    B[1] = min(B[1], A[i][1])
    i += 1
ans.append(B)

while i < n:
    ans.append(A[i])
    i += 1

print(ans)