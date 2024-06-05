'''Problem Description
Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
Your task is to find the count of good subarrays in A.'''

A = [1, 2, 3, 4, 5]
# A = [1, 2, 3]
B = 4
count = 0

pf = [0]*len(A)
pf[0] = A[0]
for i in range(1, len(A)):
    pf[i] = pf[i-1] + A[i]
print(A)
# print(pf)


for i in range(len(A)):
    sum = 0
    for j in range(i, len(A)):
        # print('Checking for :', i, j, A[i:j+1], len(A[i:j+1]))
        sum += A[j]
        length = j-i+1
        # checking for even length subarray
        if (length % 2 == 0 and sum < B) or (length % 2 != 0 and sum  > B) :
            print('Checking for :', i, j, A[i:j + 1], len(A[i:j + 1]))
            print(f"{j - i+1}")
            print("count up by 1")
            count +=1
            print(A[i:j+1],'len: ', len(A[i:j+1]),'sum: ',sum)
print(count)