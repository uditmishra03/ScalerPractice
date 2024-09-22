arr = [1, 2, 3]

n =len(arr)
ans =0
for i in range(n):
    contribution = (i+1) * (n-i)
    ans += arr[i] * contribution

print('Final ans:', ans)