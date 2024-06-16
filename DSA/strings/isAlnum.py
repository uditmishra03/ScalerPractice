'''Problem Description
You are given a function isalpha() consisting of a character array A.
Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.'''

# Input 1:
# A =['A']
# A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']
# Input 2:
A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']
def checkAlnum(lst):
    isAlnum = None
    for each in A:
        if (ord(each) >= 65 and ord(each) <= 90) or (ord(each) >= 97 and ord(each) <= 122) or (ord(each) >= 48 and ord(each) <= 57):
            isAlnum = True
        else:
            return 0
            # isAlnum = False
            # print(each)
            # break
    if isAlnum:
        return 1
    # print(isAlnum)

print(checkAlnum(A))