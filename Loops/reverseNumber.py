'''Reverse a Number:

Input: A positive integer n

Output: Print the reverse of the number'''

num = int(input("Enter the number: "))
# num = 45721
# using slicing method on the string.
# num = int(str(num)[::-1])
# print(num)

# using loop
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10

print(rev)
