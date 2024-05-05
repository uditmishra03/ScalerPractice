'''Pattern Printing:

Input: A positive integer n

Output: Print triangle pattern of numbers or stars using nested loops (e.g., a right triangle of asterisks)'''
num = int(input("Enter the size of triangle: "))

# num =4

for i in range(1, num+1):
    for j in range(i):
        print('*', end ='')
    if i != num:
        print()