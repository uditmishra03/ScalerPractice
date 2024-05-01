'''Problem Description:

Write a function to check whether a given number n as an input to the function is a perfect number or not. If the given integer is a perfect number return 1 else return 0.

Note: In number theory, a perfect number is a positive integer that is equal to the sum of its proper positive divisors, that is, the sum of its positive divisors excluding the number itself (also known as its aliquot sum).

Input Format:

The only argument to the function is an integer n.
Output Format:

Print out 1 if the number is perfect else 0 in integer format.
Sample Input:

6
Sample Output:

1'''

num = int(input("Enter the number: "))

sumOfDivisors = 0
for i in range(1, (num//2+1)):
    print(i)
    if num % i == 0:
        sumOfDivisors +=i

# print(sumOfDivisors)

if num > 0 and sumOfDivisors == num:
    print('1')
else:
    print('0')