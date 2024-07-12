# from CountTheSetBits import checkBit


def checkBit(N, i):
    if N & (1 <<i) == 0:
        return False
    else:
        return True
    


arr = [4,5,5,4,1,6,6, 1, 9]

ans = 0

for bit in range(31):
    count = 0
    for j in range(len(arr)):
        if checkBit(arr[j], bit) == True:
            count +=1
            
    
    if count % 2 == 1:
        # print('Setting bit at: ', bit)
        ans = ans | 1 << bit

print(ans)        




