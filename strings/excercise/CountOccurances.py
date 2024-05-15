'''Exercise 10: Write a program to count occurrences of all characters within a string'''

str1 = "wallaby"


def countChars(string):
    str1_dict = {}
    for char in string:
        # print(f" {char}: {str1.count(char)}")
        str1_dict[char] = string.count(char)
    return str1_dict


print(countChars(str1))
