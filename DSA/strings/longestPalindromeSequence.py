'''Problem Description
Given a string A of size N, find and return the longest palindromic substring in A.
Substring of string A is A[i...j] where 0 <= i <= j < len(A)
Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
Incase of conflict, return the substring which occurs first ( with the least starting index).'''

# A = "aaaabaaa"
A='aaaabaaa'
# A= 'abb'
# A= 'abcbedrardea'
n = len(A)
print('Total string len: ',n)
if n % 2 == 0:
    evenLength = True
else:
    evenLength = False
ans = 0
for i in range(n):
    # print('Checking for i: ', i)
    if evenLength:
        left, right = i, i+1
    else:
        left, right = i, i
    print(left, right)
    while left >= 0 and right < n:
        if A[left] != A[right]:
            break
        else:
            left -=1
            right +=1
    actual_start = left +1
    actual_end = right -1
    # print(actual_start, actual_end)
    length = actual_end - actual_start +1
    print('Palindrom len: ', length)
    # palindrome = A[actual_start:actual_end+1]
    ans = max(ans, length)
    if ans == length:
        palindrome = A[actual_start:actual_end + 1]
print(ans)
print(palindrome)