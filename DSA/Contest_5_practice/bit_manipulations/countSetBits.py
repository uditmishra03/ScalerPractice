n = 7

def checkBit(N, i):
    if N & 1 <<i == 0:
        return False
    else:
        return True

count = 0
for i in range(31):
    if checkBit(n, i) == True:
        count +=1
    
print("Set bits count: ", count)