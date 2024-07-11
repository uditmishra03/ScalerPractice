# A = 4
# B = 6

A, B = 6, 7

def findgcd(A, B):
    if B == 0:
        return A
    ans = findgcd(B, A%B)
    return ans


# def hcf(a, b):
#     num = min(a, b)
#     while True:
#         if a % num ==0 and b%num == 0:
#             return num
#         else:
#             num -=1


print(findgcd(A, B))