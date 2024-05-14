'''Exercise 12: Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.'''

fibo = [0,1]

length = 10

for i in range(2, length+1):
    fibo.append(fibo[i-1] + fibo[i-2])

for each in fibo:
    print(each, end =',  ')