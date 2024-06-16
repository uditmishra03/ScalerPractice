'''Problem Description
You are given a character string A having length N, consisting of only lowercase and uppercase latin letters.
You have to toggle case of each character of string A. For e.g 'A' is changed to 'a', 'e' is changed to 'E', etc.∑'''

A = "Hello"

result = ''
for i in range(len(A)):
    if ord(A[i]) >= 65 and ord(A[i]) <= 90:
        result += (chr(ord(A[i]) + 32))
    else:
        result += (chr(ord(A[i]) - 32))

print(result)