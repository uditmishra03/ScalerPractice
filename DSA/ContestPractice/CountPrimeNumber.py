'''Problem Description
You will be given an integer n. You need to return the count of prime numbers less than or equal to n.'''
import math

num = int(input("Enter the number to find if it is prime or not: "))

count = 0
primeNumbers = []
if num == 1:
    primeNumbers = None
for each in range(2, num + 1):
    isPrime = True
    for divisors in range(2, int(math.sqrt(each)) + 1):
        if each % divisors == 0:
            isPrime = False
            break
    if isPrime:
        primeNumbers.append(each)
        count += 1

print(f"\n*** Total number of prime number count till {num} are {count}, these are: {primeNumbers}***")
