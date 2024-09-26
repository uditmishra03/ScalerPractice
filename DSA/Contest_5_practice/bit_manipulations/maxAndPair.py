arr = [26, 13, 28, 23, 27, 7, 25]

ans = 0

n = len(arr)

def checkBit(N, i):
    if N & 1 <<i == 0:
        return False
    else:
        return True

   
for i in range(31, -1, -1):
    count = 0
    for j in range(n):
        if checkBit(arr[j], i) == True:
            count +=1

    if count >= 2:
        ans = ans | 1 << i
        for j in range(n):
            if checkBit(arr[j], i) == False:
                arr[j] = 0
    

print('Final ans', ans)

