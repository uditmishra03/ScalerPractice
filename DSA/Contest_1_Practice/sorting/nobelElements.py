A = [3, 2, 1, 3]

A.sort(reverse=True)
print(A)


less = 0
count = 0

if A[0] == 0:
    count +=1

for i in range(1, len(A)):
    if A[i] != A[i-1]:
        less=i
    else:
        pass
        # the value of less remains same.
    if A[i] == less:
        print('yes found it')
        count +=1

print(less)
print(count)
