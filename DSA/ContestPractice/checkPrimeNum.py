'''Problem Description
Given a number A. Return 1 if A is prime and return 0 if not.

Note :
The value of A can cross the range of Integer.'''
import math

num = int(input("Enter the number to find if it is prime or not: "))

# print('we\'ll check till: ', int(math.sqrt(num)))
isPrime = True
for i in range(2, int(math.sqrt(num))+1):
    if num % i == 0:
        print(f"{num} got divided by {i}")
        isPrime = False
        break

if isPrime:
    print(f"{num} is a prime number.")
else:
    print(f"so, {num} is not a prime number.")
