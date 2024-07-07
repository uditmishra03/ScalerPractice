'''Problem Description
Given an array A of length N where all the elements are distinct and are in the range [1, N+2].

Two numbers from the range [1, N+2] are missing from the array A. Find the two missing numbers.'''

# A = [3, 2, 4]
# A = [5, 1, 3, 6]
A= [4,5,2,9,3,7,8,11,10]

def checkBit(N, i):
    if N & (1 << i) == 0:
        return False
    else:
        return True
    
n = len(A)
max_range = n+2

XOR = 0 
for i in range(n): 
    # print(A[i])
    XOR ^= A[i] 
print('Xor of array:', XOR)
for i in range(1,max_range+1): 
    # print(i)
    XOR ^= i 
print('UpdaTED Xor :', XOR)


pos = 0
for i in range(32):
    if checkBit(XOR, i) == True:
        pos = i
        break

print('first bit set: ', pos)


x, y = 0, 0

for i in range(n): 
    if checkBit(A[i], pos) == True: 
        # XOR of first set in arr[]  
        x = x ^ A[i]   
    else: 
        # XOR of second set in arr[]  
        y = y ^ A[i]   

for i in range(1,max_range+1): 
    if checkBit(i, pos)== True:
        print('set', i) 
        # XOR of first set in arr[] and 
        # {1, 2, ...n } 
        x = x ^ i  
    else: 
        print('unset: ', i)
        # XOR of second set in arr[] and 
        # {1, 2, ...n }  
        y = y ^ i 
ans = [0]*2
if x < y:
    ans[0]=x
    ans[1]=y
    
else:
    ans[0]=y
    ans[1]=x
    
print(ans)