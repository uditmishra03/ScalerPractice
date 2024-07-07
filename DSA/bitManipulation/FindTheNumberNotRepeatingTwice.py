'''Problem Description
Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
Find the two integers that appear only once.

Note: Return the two numbers in ascending order.'''


# A = [1, 2, 4, 1, 2, 3]
A = [1, 2]

def checkBit(N, i):
    if N & (1 << i) == 0:
        return False
    else:
        return True


n = len(A)
# 1. Take xor of all elements.
xorAll = 0
for i in range(n):
    xorAll = xorAll ^ A[i]

print(xorAll)

# 2. Find any set bit position in xorAll
pos = 0
for i in range(32):
    if checkBit(xorAll, i) == True:
        pos = i
        break

print('Found the set bit in ', xorAll, 'is:', pos)

# 3. Split the array on the basis of posth bit.
num1, num2 = 0, 0
for i in range(n):
    if checkBit(A[i], pos) == True:
        num1 = num1 ^ A[i]
    else:
        num2 = num2 ^ A[i]

print(f"num1: {num1}\nnum2: {num2}")

print('Unique numbers of the array are: ')
# 4. Print the unique numbers. 
if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)



