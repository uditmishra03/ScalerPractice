'''Problem Description
Given two binary strings A and B. Return their sum (also a binary string).'''

A= '110'
B = '11'
# A = "1010110111001101101000"
# B = '1000011011000000111100110'

print(A, B, sep = '\n ')
max_len = max(len(A), len(B))

B = '0'*(max_len-len(B)) + B
A = '0'*(max_len-len(A)) + A

print(A)
print(B)
# print(A[0])
sum = 0
carry = 0
result =''
for bit in range(max_len-1, -1, -1):
    print('***bit: ', max_len-bit-1, '--> ', int(A[bit]), int(B[bit]))
    sum = int(A[bit]) + int(B[bit]) + carry
    if sum > 1:
        carry = sum //2
        sum = sum %2
    # if sum == 1:
    #     carry = 0
    #     sum = 1
    # if sum == 2:
    #     carry = 1
    #     sum = 0
    # if sum == 3:
    #     carry = 1
    #     sum = 1
    print('sum: ', sum, 'carry --> ', carry, "\n")
    result = str(sum) + result
if carry > 0:
    result = str(carry) + result

print(result)