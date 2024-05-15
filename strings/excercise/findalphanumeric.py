"""Exercise 17: Find words with both alphabets and numbers
Write a program to find words with both alphabets and numbers from an input string.

Given:

str1 = "Emma25 is Data scientist50 and AI Expert"""

str1 = "Emma25 is Data scientist50 and AI Expert"

for each in str1.split():
    isalnum = True
    for char in each:
        if not char.isalnum():
            isalnum = False
    print(isalnum)
    # if isalnum:
    #     print(each)