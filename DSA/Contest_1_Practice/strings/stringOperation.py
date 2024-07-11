'''Problem Description
Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:

Concatenate the string with itself.
Delete all the uppercase letters.
Replace each vowel with '#'.
You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.

NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.'''

# A="aeiOUz"
A = 'AbcaZeoB'
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# Concatenate the string with itself.
A = A + A
print(A)

# Delete all the uppercase letters.
A_removed_UC = ''
for char in A:
    # print(char)
    if 97 <= ord(char) <= 122:
        A_removed_UC += char

print(A_removed_UC)
A = A_removed_UC
print(A)

A_replaced_vowels = ''
for char in A:
    if char in vowels:
        char = '#'
    A_replaced_vowels += char

A = A_replaced_vowels
print(A)
