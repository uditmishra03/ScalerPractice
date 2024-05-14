'''Exercise 1A: Create a string made of the first, middle and last character
Write a program to create a new string made of an input string’s first, middle, and last character'''
import math

str1 = "James"

length = len(str1)
if length > 0:
    first = 0
    last = length-1
    if length % 2 == 0:
        mid = int(length/2)
    else:
        mid = int(math.floor(length/2))

print(first, last, mid)
print(str1[first],  str1[mid], str1[last], sep='')

