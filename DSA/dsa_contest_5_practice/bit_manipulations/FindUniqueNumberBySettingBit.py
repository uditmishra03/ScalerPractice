arr = [1, 2, 3, 1, 3, 2, 9, 9, 32]

def checkBit(N, i):
    if N & 1 << i == 0:
        return False
    else:
        return True
    

ans = 0
for i in range(31):
    bit_count =0
    
    for j in range(len(arr)):

        if checkBit(arr[j], i) == True:
            bit_count +=1
        
    if bit_count % 2 ==1:
        ans = ans | 1 <<i
    

print('Final ans:', ans )
