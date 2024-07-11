A =[2, 6,3,1]

A.sort(reverse= True)
print(A)

ans = 0
for i in range(len(A)):
    ans += (i+1)* A[i]

print(ans)