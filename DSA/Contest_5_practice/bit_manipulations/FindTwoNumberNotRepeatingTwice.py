arr = [10, 8, 8, 9 , 12, 9, 6, 11, 10, 6, 12, 17, 11, 17, 22, 55]

n = len(arr)
# print(n)

def checkBit(N, i):
    if N & 1 <<i == 0:
        return False
    else:
        return True
    

# 1. Find the xorall for all the elements.

# 2. Find the first bit which is set in xorall.

# 3. Based on the first bit set, split the array into two parts. 

xorall =0
for i in range(n):
    xorall ^= arr[i]

print(xorall)

for i in range(31):
    if checkBit(xorall, i) == True:
        pos = i
        break

print(pos)

num1, num2 = 0, 0
for i in range(n):
    if checkBit(arr[i], pos) == True:
        num1 ^= arr[i]
    else:
        num2 ^= arr[i]


print("Unique numbers are: ", num1, num2)