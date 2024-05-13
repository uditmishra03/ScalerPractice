'''Exercise 13: Find the factorial of a given number
Write a program to use the loop to find the factorial of a given number.'''

num = int(input("Enter the number: "))

factorial = 1
for i in range(num, 0, -1):
    factorial *=i

print(f"{num}! is {factorial}")