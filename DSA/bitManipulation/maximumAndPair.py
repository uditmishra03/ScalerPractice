'''Problem Description
Given an array A. For every pair of indices i and j (i != j), find the maximum A[i] & A[j].'''


def checkBit(N, i):
    if N & (1 << i) == 0:
        return False
    else:
        return True


# A = [53, 39, 88]
A = [38, 44, 84, 12] 

n = len(A)

result = []
ans = 0
reducedA= []
for i in range(31, -1, -1):
    count =0
    for j in range(n):
        if checkBit(A[j], i) == True:
            # count +=1
            reducedA.append(A[j])
        # else:
        #     print(f"bit not set for:  {A[j]}")
            # A.pop(j)
    # print('Updated list:', A)
    print(reducedA)
    # print('count of bit:', i, 'is: ', count)
    if len(reducedA) >=2:
        result = reducedA
        # ans = ans | (1 << i)      # setting the bit.
        # for j in range(n):
        #     if checkBit(A[j], i) == False:
        #         A[j] = 0        # making the value of element as zero which is not contributing to the ans.

print(result[0] & result[1])
print(ans)
