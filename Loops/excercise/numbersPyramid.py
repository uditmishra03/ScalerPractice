'''Exercise 2: Print the following pattern
Write a program to print the following number pattern using a loop.

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5'''

# num = int(input("Enter the number/size : "))
num =5
for i in range(1, num+1):
    # print('i--> ', i)
    for j in range(1, i+1):
        if j == i:
            print(j, end='')
        else:
            print(j, end = ' ')
    if i != num:
        print()