# A = [1, 2, 3]
A = [17, 100, 11]
n = len(A)


mod = (10**9 +7)
count = [0]*1001
for a in A:
    count[a]+=1

ans = 0

for i in range(1,1001):
    for j in range(1, 1001):
        val = i%j
        temp = count[i] * count[j] * val
        ans = ((ans%mod)+ (temp%mod))% mod

print(ans)