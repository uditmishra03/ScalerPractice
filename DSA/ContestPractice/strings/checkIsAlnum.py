'''roblem Description
You are given a function isalpha() consisting of a character array A.

Return 1 if all the characters of a character array are alphanumeric (a-z, A-Z, and 0-9) else, return 0.'''

# A = ['S', 'c', 'a', 'l', 'e', 'r', 'A', 'c', 'a', 'd', 'e', 'm', 'y', '2', '0', '2', '0']

A = ['S', 'c', 'a', 'l', 'e', 'r', '#', '2', '0', '2', '0']

for char in A:
    if 'a' <=char <='z' or 'A' <= char <= 'Z' or 48 <= ord(char) <= 57:
        print('yes')
    else:
        print(char, 'no', type(char))
    # print(char)