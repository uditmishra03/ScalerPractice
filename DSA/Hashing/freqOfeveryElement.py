'''Problem Description
Given an array A. You have some integers given in the array B.
For the i-th number, find the frequency of B[i] in the array A and return a list containing all the frequencies.'''

# A = [1, 2, 1, 1]
# B = [1, 2]
A = [2, 5, 9, 2, 8]
B = [3, 2]
freq = {}
for i in A:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] +=1

# print(freq)
ans = []
for q in B:
    if q in freq:
        ans.append(freq[q])
    else:
        ans.append(0)

print('final ans:', ans)