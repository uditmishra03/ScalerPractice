'''Given a binary string A. It is allowed to do at most one swap between any 0 and 1. Find and return the length of the longest consecutive 1’s that can be achieved.'''
# A = "111000"
A = "111011101"
one_count, ans = 0, 0
n = len(A)
for each in A:
    if each == '1':
        one_count +=1
print('One count: ', one_count)
if one_count == len(A):
    ans = len(A)

for i in range(n):
    if A[i] == '1':
        continue
    else:
        left, right = 0, 0
        j = i+1
        while j < n and A[j] == '1':
            right +=1
            j +=1
        j = i-1
        while j >= 0 and A[j] == '1':
            left += 1
            j -= 1

        if left + right == one_count:
            ans = max(ans, left+right)
        else:
            ans = max(ans, left+right+1)

print('ans: ', ans)