'''Exercise 11: Write a program to display all prime numbers within a range
Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers'''
import math

start = int(input("Enter the starting point: "))
end = int(input("Enter the ending point: "))


# start = 2
# end = 20
primenumbers = []
if start == 1:
    start = 2
for num in range(start, end+1):
    # print('Checking for : ', num)
    isPrime = True
    for i in range(2, int(math.sqrt(num))+1):
        # print('divisor --> ', i)
        if num % i == 0:
            # print("is not a prime")
            isPrime = False
    if isPrime:
        primenumbers.append(num)

print(f"Prime numbers i.e., {len(primenumbers)} between {start} and {end} are:")

# print(primenumbers[-1])
for each in primenumbers:
    if each == primenumbers[-1]:
        print(each, end='')
    else:
        print(each, end = ', ')