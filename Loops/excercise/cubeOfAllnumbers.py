'''Exercise 16: Calculate the cube of all numbers from 1 to a given number
Write a program to rint the cube of all numbers from 1 to a given number'''

number = int(input("Enter the number: "))

for each in range(1,number+1):
    print(f"Current Number is : {each}  and the cube is {each ** 3}")