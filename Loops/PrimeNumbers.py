import math

num = int(input("Enter the number: "))

isPrime = True
for i in range(2, int(math.sqrt(num)+1)):
    # print(i)
    if num % i == 0:
        isPrime = False
if isPrime == True:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    #
    # else:
    #     print(num, "is not a prime number")