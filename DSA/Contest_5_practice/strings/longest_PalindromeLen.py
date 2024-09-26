# A = "abba"
# A ='dccbcdaac'

A = 'xyracecarabbagh'

n = len(A)

if n == 0:
    print('Not found. -1')
else:
    max_len, start_idx = 1, 0

    for i in range(1, n):
        #Chekcing for even length palindrome.
        left, right = i-1, i
        while left >=0 and right < n and A[right]==A[left]:
            palin_len = right-left+1

            if max_len < palin_len:
                max_len = palin_len
                start_idx = left
            left -=1
            right +=1

        
        #Chekcing for odd len palindorme length.
        left, right = i-1, i+1
        while left >=0 and right < n and A[right]==A[left]:
            palin_len = right-left+1

            if max_len < palin_len:
                max_len = palin_len
                start_idx = left
            left -=1
            right +=1
        
    print(f"Longest Palindrome: {A[start_idx: start_idx + max_len]}, of length: {max_len}")
        