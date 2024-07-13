'''Scooby has 3 three integers A, B, and C.

Scooby calls a positive integer special if it is divisible by B and it is divisible by C. You need to tell the number of special integers less than or equal to A.'''

A = 12
B = 3
C = 2

# A = 6
# B = 1
# C = 4

'''
1. Find gcd
2. find LCM
3. Return the floor value of A/LCM.
'''

def findgcd(A, B):
    if B == 0:
        return A
    ans = findgcd(B, A%B)
    return ans

gcd = findgcd(B, C)
print('GCD: ', gcd)

lcm = (B*C)/gcd
print('lcm:', int(lcm))

ans = int(A//lcm)
print('final ans: ', ans)