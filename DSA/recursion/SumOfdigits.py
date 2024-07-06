'''Problem Description
Given a number A, we need to find the sum of its digits using recursion.'''

num = 123456

def sumOfDigits(num):
    ans = 0

    if num == 0:
        return 0
    else:
        return (num % 10+ sumOfDigits(num//10))
            


print(sumOfDigits(num))