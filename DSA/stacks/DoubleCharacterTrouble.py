'''Problem Description
You have a string, denoted as A.

To transform the string, you should perform the following operation repeatedly:
Identify the first occurrence of consecutive identical pairs of characters within the string.
Remove this pair of identical characters from the string.
Repeat steps 1 and 2 until there are no more consecutive identical pairs of characters.
The final result will be the transformed string.'''


A = "abccbc"
# A = "ab"

char_stk = []

for i in A:
    if len(char_stk) ==0:
        char_stk.append(i)
    else:
        if char_stk[-1] == i:
            char_stk.pop()
        else:
            char_stk.append(i)

ans = ''
while char_stk:
    ans += char_stk[-1]
    char_stk.pop()

print("final ans:", ans[::-1])
