'''Problem Description
Given an array A of 0s and 1s of length N. Sort this array.'''

# A = [0,0,1,0,1,1,0]
A = [1,0]

zeros =0
for i in A:
    if i == 0:
        zeros +=1

print('total zeros: ', zeros)
ans = [0]*len(A)
for i in range(0, zeros):
    ans[i] = 0

for i in range(zeros, len(A)):
    ans[i] = 1

print(ans)

    

