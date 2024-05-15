"""Exercise 16: Removal all characters from a string except integers
Given:

str1 = 'I am 25 years and 10 months old'"""

str1 = 'I am 25 years and 10 months old'

numerics =''

for each in str1:
    # Both functions will work.
    # if each.isdigit():
    if each.isnumeric():
        numerics += each

print(numerics)