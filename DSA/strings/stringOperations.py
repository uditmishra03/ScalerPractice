'''Problem Description
Akash likes playing with strings. One day he thought of applying following operations on the string in the given order:
Concatenate the string with itself.
Delete all the uppercase letters.
Replace each vowel with '#'.
You are given a string A of size N consisting of lowercase and uppercase alphabets. Return the resultant string after applying the above operations.
NOTE: 'a' , 'e' , 'i' , 'o' , 'u' are defined as vowels.'''

#
A="aeiOUz"
# A="AbcaZeoB"
# A= "Udit Mishra"
# concatenation with itself.
A +=A

# print(A)
A = ('').join(A.split(' ')).strip()
# print(A)
result =''
vowels = ['a', 'e', 'i', 'o', 'u']

# Removal of Uppercase letters.
for i in range(len(A)):
    # print(A[i])
    if ord(A[i]) >= 97 and ord(A[i]) <= 122 :
        result += A[i]

# print(result)
resultant_str =''
# replacing vowels with #
for i in range(len(result)):
    # print(result[i])
    if result[i] in vowels:
        resultant_str += '#'
    else:
        resultant_str += result[i]
    # print(resultant_str)
# print(result)
print(resultant_str)


