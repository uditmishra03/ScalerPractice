''' Fibonacci Sequence :

Input: A non-negative integer n

Output: Print the first n numbers in the Fibonacci sequence (0, 1, 1, 2, 3, 5, ...)'''

number = int(input("Enter the number: "))

fibo = [0, 1]

for i in range(2, number):
    # print((fibo[i-1]), fibo[i-2])
    fibo.append(fibo[i-1] + fibo[i-2])

for i in range(len(fibo)):
    # print(i)
    if i == number-1:
        print(fibo[i], end='')
    else:
        print(fibo[i], end=', ')