A = [3, 2, 4]
# A = [5, 1, 3, 6]
# A= [4,5,2,9,3,7,8,11,10]

def checkBit(N, i):
    if N & (1 << i) == 0:
        return False
    else:
        return True
    

n = len(A)
max_range = n+2
# find xor of the array
xor =0
for i in range(n):
    xor ^= A[i]

print('xor of array:', xor)

for i in range(max_range+1):
    xor ^=i

print('xor of max range array:', xor)

# find the set bit of xor.

for i in range(32):
    if checkBit(xor, i) == True:
        pos =i
        break

print('Set bit of xor is ', i)

# divide the array into two parts based on the set bit of xor.

num1, num2 = 0, 0
for i in range(n):
    if checkBit(A[i], pos) == True:
        # print('with set bit', A[i])
        num1 ^=A[i]
    else:
        # print('with unset bit', A[i])
        num2 ^=A[i]

# print('Now for full range')
# now do the same thing for max range elements.
for i in range(1, max_range+1):
    # print(i)
    if checkBit(i, pos) == True:
        # print('with set bit', i)
        num1 ^=i
    else:
        # print('with unset bit', i)
        num2 ^=i

print(num1, num2)
