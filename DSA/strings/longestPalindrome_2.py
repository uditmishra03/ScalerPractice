# A = "aaaabaaa"
# A = 'aaaabaaa'
# A= 'abb'
# A= 'abcbedrardea'
# A = 'hghjbaccabererq'
# A = 'banana'
A ='dccbcdaac'
n = len(A)

if n == 0:
    print('None found')
    # return ""
max_len = 1
starting_index = 0
for i in range(1, n):
    # Check for even length palindrome centered at i-1 and i
    left = i - 1
    right = i
    while left >= 0 and right < n and A[left] == A[right]:
        print('even', i)
        palindrome_len = right - left + 1
        if palindrome_len > max_len:
            starting_index = left
            max_len = palindrome_len
        left -= 1
        right += 1
        print(left, right, max_len)
    # Check for odd length palindrome centered at i
    left = i - 1
    right = i + 1
    while left >= 0 and right < n and A[left] == A[right]:
        print('odd', i)
        palindrome_len = right - left + 1
        if palindrome_len > max_len:
            starting_index = left
            max_len = palindrome_len
        left -= 1
        right += 1
        print(left, right, max_len)
print(A[starting_index:starting_index + max_len])
# return A[start:start + max_len]