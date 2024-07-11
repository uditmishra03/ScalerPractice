A= '110'
B ='1'

max_len = max(len(A), len(B))
print(max_len)

A = '0'*(max_len-len(A)) + A
# print(A)
B = '0'*(max_len-len(B)) + B
print(A, B, sep='\n')
result = ''
sum, carry = 0, 0
for bit in range(max_len-1, -1, -1):
    sum = int(A[bit]) + int(B[bit]) + carry
    # print(sum)
    if sum >= 1:
        carry = sum //2
        sum = sum %2
    result = str(sum)+ result
# print(carry)
if carry > 0:
    result = str(carry) + result

print(result)