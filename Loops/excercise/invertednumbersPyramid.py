'''Exercise 7: Print the following pattern
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1'''
num = int(input("Enter the size of pyramid: "))
# num = 5

for i in range(num, 0, -1):
    # print(i)
    for j in range(i, 0, -1):
        if j == 1:
            print(j, end='')
        else:
            print(j, end =' ')
    if i != 1:
        print()