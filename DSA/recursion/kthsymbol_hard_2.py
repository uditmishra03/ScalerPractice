import sys
sys.setrecursionlimit(10**6)

def find(n, k):
    print('Calling find func at line 5', n, k)
    if k == 0:
        return 0
    val = find(n - 1, k // 2)
    print('from here at 9')
    if k % 2 == 0:
        print(val)
        return val
    return 1 - val


# A = 3
# B = 0
A = 4
B = 4
print(find(A, B))