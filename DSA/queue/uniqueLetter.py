from collections import deque, defaultdict

'''Problem Description
Imagine you're a teacher. You ask students to call out a letter one by one. After each letter, you jot down the very first letter that's only been called out once. If all letters have been repeated, you write "#".'''

A = "abadbc"
# # Input 2:

# A = "abcabc"
def UniqueLetter(A):
    q= deque()
    hm = defaultdict(int)

    ans = ''

    for char in A:
        # print(char)
        hm[char] +=1
        q.append(char)

        while q and hm[q[0]] > 1:
            q.popleft()
        if q:
            ans+=q[0]
        else:
            ans+='#'
    
    return ans

print('Final ans:', UniqueLetter(A))

