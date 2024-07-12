arr = [4, 5, 4, 1, 6, 6, 5, 9]

'''
1. Take the xor of all elements.

2. find the position of set bit in xor result.

3. based on the set bit, divide the arr into two parts and find the two numbers.
'''

def checkBit(n, i):
    if n & (1 << i) == 0:
        return False
    else:
        return True

xor =0
for i in range(len(arr)):
    xor ^= arr[i]

print(xor)

for i in range(32):
    if checkBit(xor, i) == True:
        pos = i
        break

print("first set bit found at: ", pos)


num1, num2 = 0, 0

for i in range(len(arr)):
    if checkBit(arr[i], pos) == True:
        num1 ^=arr[i]
    else:
        num2 ^=arr[i]

print('Non repetive elements:', num1,num2, sep=', ')


