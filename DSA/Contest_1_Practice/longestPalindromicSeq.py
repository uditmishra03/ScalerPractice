# A = 'aaaabaaa'
# A= 'abb'
# A= 'abcbedrardea'
# A = 'hghjbaccabererq'
# A= ''
# A = "abba"
A ='dccbcdaac'

n = len(A)
if n == 0:
    max_len = 0
    starting_idx = 0
    print("None found.")

else:
    max_len = 1
    starting_idx = 0

    for i in range(1, n):
        # Check for even length palindrome.
        left = i - 1
        right = i
        while left >= 0 and right < n and A[left] == A[right]:
            palindrome_len = right - left + 1
            if max_len < palindrome_len:
                max_len = palindrome_len
                starting_idx = left
            left -= 1
            right += 1

        # Check for odd length palindrome.
        left = i - 1
        right = i + 1
        while left >= 0 and right < n and A[left] == A[right]:
            palindrome_len = right - left + 1
            if max_len < palindrome_len:
                max_len = palindrome_len
                starting_idx = left
            left -= 1
            right += 1

    print(f"Longest Palindrome: {A[starting_idx: starting_idx + max_len]}, of length: {max_len}")
