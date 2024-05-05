import math
'''Prime Number Check:

Input: A positive integer n

Output: Print "Yes" if the number is prime (divisible only by 1 and itself), "No" otherwise'''

number = int(input("Enter the number: "))

isPrime = True
for i in range(2, int(math.sqrt(number))+1):
    if number % i == 0:
        isPrime = False

if isPrime:
    print("Yes")
else:
    print("No")