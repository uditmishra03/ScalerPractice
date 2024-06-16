'''You are given a string A of size N.
Return the string A after reversing the string word by word.
NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.'''

A = "the sky is blue"


# A = 'crulgzfkif gg ombt vemmoxrgf qoddptokkz op xdq hv'

def reverseStringByWords(A):
    A_list = A.split()
    A_rev= A_list[::-1]
    # print(A_rev)
    result = ' '.join(A_rev)
    print(result)


print(reverseStringByWords(A))