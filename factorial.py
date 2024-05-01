num = int(input("Enter the number: "))
original_num = num
factorial = 1

while num >= 1:
    factorial *=num
    num -=1

print("Factorial of ", original_num,"is : ", factorial)