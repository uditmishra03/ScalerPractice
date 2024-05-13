'''Exercise 3: Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)'''

num = int(input("Enter the number/size : "))
counter = num
sum =0
# for i in range(num+1):
#     sum +=i

while counter >0:
    sum +=counter
    counter -=1

print(f"\nsum of first {num} is : {sum}")