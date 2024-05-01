#!/usr/bin/python3

num = int(input("Enter the number: "))

sum =0
i = 1
while  i<=num:
    if (i%2 == 0):
        sum+=i
        print(i, sum)
    i+=1
#for i in range(1, num+1):
#    if (i %2 == 0):
#        sum+=i
#        print(i, sum)
#
print("Sum of numbers: ", sum)

