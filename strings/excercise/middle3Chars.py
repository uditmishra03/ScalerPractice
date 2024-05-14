'''Exercise 1B: Create a string made of the middle three characters
Write a program to create a new string made of the middle three characters of an input string.'''

# str1 = "JhonDipPeta"
str1 = "JaSonAy"

# print(len(str1))

mid = int(len(str1)/2)
# print(mid)

# print(str1[mid])

new_str = str1[mid-1:mid+2]
print(new_str)