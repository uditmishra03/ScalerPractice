#!/usr/bin/python3

num = int(input())

# Printing numbers from num to 1, using for loop without using negative jump
for i in range(0, num):
    print(num-i, end=' ')

print()
print("*"*num, end='')
print()
while num>=1:
    print(num, end=' ')
    num-=1

