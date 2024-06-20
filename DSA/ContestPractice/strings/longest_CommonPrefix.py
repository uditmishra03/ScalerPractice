# A = ["abcdefgh", "aefghijk", "abcefgh"]
A = ["abeeab", "abere", "abacd"]
n= len(A)
if n == 0:
    result = A[0]
else:
    min_len = len(A[0])
    # print(min_len)
    for i in range(1, len(A)):
        # print(A[i])
        if min_len > len(A[i]):
            min_len = len(A[i])

# print(min_len)
subString_len =0
for i in range(min_len):
    if A[0][i]==A[1][i]:
        subString_len +=1

prefix = A[0][:subString_len]
prefixFound = True
for i in range(2, len(A)):
    print(A[i])
    if not A[i].startswith(prefix):
        prefixFound = False

if prefixFound:
    print(prefix)
else:
    print('No prefix exist.')
