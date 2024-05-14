'''Exercise 18: Print the following pattern
Write a program to print the following start pattern using the for loop

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*'''

num = 5
for i in range(1, num+1):
    for j in range(i):
        if j == i-1:
            print('*', end ='')
        else:
            print('*', end=' ')
    print()
for i in range(num-1, 0, -1):
    for j in range(i):
        if j == i - 1:
            print('*', end = '')
        else:
            print('*', end=' ')
    if i !=1:
        print()
