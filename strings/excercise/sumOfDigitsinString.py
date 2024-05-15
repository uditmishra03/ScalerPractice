"""Exercise 9: Calculate the sum and average of the digits present in a string
Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.

"""
str1 = "PYnative29@#8496"

sum = 0
count = 0
for char in str1:
    if char.isnumeric():
        sum += int(char)
        count +=1

print(f"Sum of all digits in \'{str1}\' is {sum} and Average is {round(sum/count, 2)}")
