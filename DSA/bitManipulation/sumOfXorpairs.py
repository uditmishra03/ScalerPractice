'''Problem Description
Given an array A of N integers. Find the sum of bitwise XOR all pairs of numbers in the array.

Since the answer can be large, return the remainder after the dividing the answer by 109+7.'''

# A = [1, 2, 3]
A =[7,3, 5]

def checkBit(N, i):
    if N & (1 << i) == 0:
        return False
    else:
        return True
    

ans = 0
for i in range(31, -1, -1):
    set, unset = 0, 0
    for num in A:
        if checkBit(num, i) == True:
            set +=1
        else:
            unset +=1
    
    ans +=set*unset *(1<<i)

print(ans)

