arr = [26, 13, 23, 28, 27, 7, 25]

n = len(arr)

def checkbit(n, i):
    if n & (1 <<i)== 0:
        return False
    else:
        return True
    
ans = 0
for i in range(31, -1, -1):
    count = 0
    for j in range(n):
        if checkbit(arr[j], i) == True:
            count +=1

    if count >=2:
        ans |= 1<<i
        for j in range(n):
            if checkbit(arr[j], i) == False:
                arr[j] = 0
        

print(arr)
print(ans)