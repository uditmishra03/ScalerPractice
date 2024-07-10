'''Problem Description
Implement pow(A, B) % C.
In other words, given A, B and C, Find (A**B % C).'''


def power(a, b, c):
    return (a**b) % c


A = 2
B = 3
C = 3

# A = 3
# B = 3
# C = 1
def pow(A, B, C):
    # ans = 0
    if A == 0:
        return 0

    if B == 0:
        return 1
    p = power(A, B//2, C)
    # print(p)
    if B % 2 == 0:
        return (p * p) % C
    else:
        return (((p * p) % C) *A)% C
    

    


print(pow(A, B, C))