'''You are given an array A of N elements. Find the number of triplets i,j and k such that i<j<k and A[i]<A[j]<A[k]'''

A = [1, 2, 4, 3]
# A = [2, 1, 2, 3]
# A= [1,16,26,17,27,26,4]

n = len(A)
ans = 0

for i in range(1, n-1):
    smallCount , largeCount = 0, 0
    count = 0
    for j in range(0, i):
        # print(f"{i}: {A[i]};{j}: {A[j]}")
        if A[i] > A[j]:
            print("j: ", j)
            smallCount +=1
    for k in range(i+1, n):
        if A[i] < A[k]:
            print("k: ", k)
            largeCount +=1

    print(f"For ith idx: {i}, small count: {smallCount} and Large count: {largeCount}")
    count = largeCount* smallCount
    ans +=count

print('count: ', ans)
