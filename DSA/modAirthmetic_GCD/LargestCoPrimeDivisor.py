'''
Problem Description

You are given two positive numbers A and B . You need to find the maximum valued integer X such that:

X divides A i.e. A % X = 0
X and B are co-prime i.e. gcd(X, B) = 1'''


# A = 30
# B = 12

A = 5
B = 10

def findgcd(A, B):
    if B == 0:
        return A
    ans = findgcd(B, A%B)
    return ans


def findCoPrimeDivisor(a, b):
    while findgcd(a,b) != 1:
        a = int(a/findgcd(a, b))
    return a

print(findCoPrimeDivisor(A, B))