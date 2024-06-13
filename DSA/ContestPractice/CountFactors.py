# Problem Description
# Given an integer A, you need to find the count of it's factors.
#
# Factor of a number is the number which divides it perfectly leaving no remainder.
#
# Example : 1, 2, 3, 6 are factors of 6

num = int(input("Enter the number to find its factors: "))
factors = []
count = 0
for each in range(1, num+1):
    if num % each == 0:
        factors.append(each)
        count +=1

print(f"Total no. of factors of {num} are {count} which are: ", end = '')
for each in range(len(factors)):
    if each == len(factors) -1:
        print('and', each)
    else:
        print(each , end =', ')
