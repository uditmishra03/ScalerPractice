'''Exercise 4: Arrange string characters such that lowercase letters should come first
Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.'''

str1 = 'PyNaTive'
result_str_lower = ''
result_str_upper = ''
for char in str1:
    if char.islower():
        result_str_lower += char
    else:
        result_str_upper += char

print(result_str_lower+result_str_upper)