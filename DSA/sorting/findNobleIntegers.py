'''Problem Description
Given an integer array A, find if an integer p exists in the array such that the number of integers greater than p in the array equals p.'''

# Input 1:
A = [3, 2, 1, 3]
# Input 2:
# A = [1, 1, 3, 3]
print("before sorting: ", A)
A.sort()
print("After sorting: ", A)
A.reverse()
print("After reversing: ", A)

less, count = 0, 0
if A[0] == 0:
    count +=1

for i in range(1,len(A)):
    # print(A[i])
    if A[i] != A[i-1]:
        less = i
        print(A[i], 'less: ', less )
    if A[i] == less:
        count +=1

print('Count is : ', count)
if count > 0:
    print('yes: 1')
else:
    print('no: -1')