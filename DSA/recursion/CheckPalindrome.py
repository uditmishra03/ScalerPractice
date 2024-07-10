'''Problem Description
Write a recursive function that checks whether string A is a palindrome or Not.
Return 1 if the string A is a palindrome, else return 0.

Note: A palindrome is a string that's the same when read forward and backward.'''



def isPalindrome(str, left, right):
    if left >= right:
        return 1
    if str[left] != str[right]:
        return 0
    else:
        ans = isPalindrome(str, left+1, right-1)
        return ans



# A = "namanaa"
A= "strings"
n = len(A)
print(n, A[0], A[n-1])
print(isPalindrome(A, 0, n-1))
