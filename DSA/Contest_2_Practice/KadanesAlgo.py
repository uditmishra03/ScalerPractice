import sys


# A =[-2, 3, 4, -1, 5, -10, 7]  
A = [ -20, 10, -20, -12, 6, 5, -3, 8, -2 ]


ans = -sys.maxsize
sum = 0

for i in range(len(A)):
    sum = sum + A[i]
    ans = max(sum, ans)
    if sum < 0:
        sum = 0
    # print('current ans: ', ans)

print('final ans: ', ans)