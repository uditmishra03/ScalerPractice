'''Exercise 4: Write a program to print multiplication table of a given number'''

num = int(input("Enter the number : "))

# for i in range(1, 11):
#     print(f"{num} * {i} = {num*i}")

multiplier = 1
while multiplier <= 10:
    print(f"{num} * {multiplier} = {num * multiplier}")
    multiplier +=1

