from bisect import bisect_left 


def solve(A, B, C):
    for lst in C:
        lst.sort()
    ans = 1000009
    for i in range(0, A - 1):
        for j in range(0, B):
            ele = C[i][j]
            x = bisect_left(C[i + 1], ele)
            if x != B:
                ans = min(ans, C[i + 1][x] - ele)
            if x == 0:
                continue
            ans = min(ans, ele - C[i + 1][x - 1])
    return ans


A = 2
B = 2
C = [ [8, 4],
      [6, 8]]


# A = 3
# B = 2
# C = [ [7, 3],
#        [2, 1],
#        [4, 9] ]

print(solve(A, B, C))