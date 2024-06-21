'''Problem Description
You are given two lowercase strings A and B each of length N. Return 1 if they are anagrams to each other and 0 if not.

Note : Two strings A and B are called anagrams to each other if A can be formed after rearranging the letters of B.'''
#
# A = "cat"
# B = "bat"
# Input 2:
A = "secure"
B = "rescue"

def checkAnagram(A, B):
    if len(A) != len(B):
        print('No')
        # return 0
    else:
        A = A.lower()
        B = B.lower()
        print(A, B)

        A = ''.join(sorted(A))
        B = ''.join(sorted(B))

        if A == B:
            print('yes')
            # return 1
        else:
            print('No')
            # return 0

checkAnagram(A, B)
