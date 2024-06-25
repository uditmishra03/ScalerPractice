'''Problem Description
You are given a binary string A(i.e., with characters 0 and 1) consisting of characters A1, A2, ..., AN. In a single operation, you can choose two indices, L and R, such that 1 ≤ L ≤ R ≤ N and flip the characters AL, AL+1, ..., AR. By flipping, we mean changing character 0 to 1 and vice-versa.

Your aim is to perform ATMOST one operation such that in the final string number of 1s is maximized.

If you don't want to perform the operation, return an empty array. Else, return an array consisting of two elements denoting L and R. If there are multiple solutions, return the lexicographically smallest pair of L and R.

NOTE: Pair (a, b) is lexicographically smaller than pair (c, d) if a < c or, if a == c and b < d'''

A = "010"
n = len(A)
print('Original String: ', A)

# function to count 1's
def countOnes(binaryString):
    oneCount = 0
    # print(binaryString[left:right])
    for i in binaryString:
        if i == '1':
            oneCount += 1
    return oneCount

# finding the prefix for count of 1s
pf_OneCount = [0]*n
if A[0] == '1':
    pf_OneCount[0] = 1
else:
    pf_OneCount[0] = 0
for i in range(1, n):
    if A[i] == '1':
        pf_OneCount[i] = pf_OneCount[i-1] +1
    else:
        pf_OneCount[i] = pf_OneCount[i-1]

print(pf_OneCount)
# print(countOnes(A))
ans = 0
indexes = []
for i in range(0, n+1):
    for j in range(i, n+1):
        print(f"i: {i}, j: {j}, string: {A[i:j+1]}, Count of Ones: , {countOnes(A[i:j+1])}" )
