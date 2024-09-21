A = [-7, 1, 5, 2, -4, 3, 0]

n = len(A)

pfsum = [0]*n
pfsum[0] = A[0]

for i in range(1, n):
    pfsum[i] = pfsum[i-1]+ A[i]


print('prefix sum of array:', pfsum)


sfsum = [0]*n
sfsum[n-1] = A[n-1]

for i in range(n-2, -1, -1):
    sfsum[i] = sfsum[i+1]+ A[i]

print('suffix sum of array:', sfsum)


equilibriumIndexFound = False
index = 0
for i in range(n):
    if pfsum[i] == sfsum[i]:
        
        equilibriumIndexFound = True
        index = i
        break

# print(equilibriumIndexFound)

if equilibriumIndexFound == True:
    print('Yes found it:', index)
else:
    print('Did not found it: -1')