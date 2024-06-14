'''Problem Description
You are given an array A of length N and Q queries given by the 2D array B of size Q×2.
Each query consists of two integers B[i][0] and B[i][1].
For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]].'''

# A = [1, 2, 3, 4, 5]
# B = [[0, 2], [2, 4], [1, 4]   ]
A = [2, 1, 8, 3, 9, 6]
B = [[0, 3],
     [3, 5],
     [1, 3],
     [2, 4]]

evennum = [0] * len(A)
countEvennum = []

# Create a evenNum array to count the number of evenNumbers in Array based on concept of prefix sum.
if A[0] % 2 == 0:
    evennum[0] = 1
for i in range(1, len(A)):
    if A[i] % 2 == 0:
        evennum[i] = evennum[i - 1] + 1
    else:
        evennum[i] = evennum[i - 1]

print(evennum)
i = 0
for each in B:
    L, R = each[0], each[1]
    if L == 0:
        countEvennum.append(evennum[R])
    else:
        countEvennum.append(evennum[R] - evennum[L - 1])
    print(f"L: {L}, R: {R}, Range: {A[L:R + 1]}, countEvennum: {countEvennum[i]}")
    i += 1
    # print(countEvennum)
print(countEvennum)