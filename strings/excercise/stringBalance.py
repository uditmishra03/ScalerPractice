'''Exercise 7: String characters balance Test
Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.'''

s1 = "Yn"
s2 = "PYnative"

# s1 = "Ynf"
# s2 = "PYnative"

def checkBalanceStrings(str1, str2):
    isBalance = True
    for char in s1:
        if char not in s2:
            isBalance = False
    return isBalance


if checkBalanceStrings(s1, s2):
    print(f"Strings \'{s1}\' and \'{s2}\' are balanced.")
else:
    print(f"Strings \'{s1}\' and \'{s2}\' are not balanced.")
# print(test)