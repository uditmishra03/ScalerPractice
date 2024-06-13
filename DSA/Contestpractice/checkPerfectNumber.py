'''Problem Description
You are given an integer A. You have to tell whether it is a perfect number or not.

Perfect number is a positive integer which is equal to the sum of its proper positive divisors.

A proper divisor of a natural number is the divisor that is strictly less than the number.'''

num = 6
sumOfFactors = 0
for i in range(1, num):
    if num % i == 0:
        sumOfFactors += i

# print('sum of factors: ', sumOfFactors)
if num != sumOfFactors:
    print("0, \"", num, "\" is not a perfect number", sep='')
else:
    print("1, \"", num, "\" is a perfect number", sep='')
