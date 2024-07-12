

def checkBit(N, i):
    if N & (1 <<i) == 0:
        return False
    else:
        return True
    

N = 7
ans = 0
pos =[]
for i in range(32):
    if checkBit(N, i) == True:
        ans +=1
        pos.append(i)

print("No of set bits in", N, 'are', ans, 'at positions:', pos)
