'''Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).

The digits are stored such that the most significant digit is at the head of the list.'''

# a = [1, 2, 3 ]
a = [0,3,7,6,4,0,5,5,5]
print('original array: ', a)
# while a[0]==0:
#     a.pop(0)
n = len(a)
# a[n-1] = a[n-1] +1

rev_a = a[-1::-1]
print('reversed array: ', rev_a)


carry = 1
for i in range(n):
    # print('for: ', rev_a[i])
    rev_a[i] = rev_a[i] + carry
    if rev_a[i] >=10:
        carry = rev_a[i] //10
        rev_a[i] = rev_a[i] % 10
    else:
        carry = 0
    # print('updated digit: ', rev_a[i])
if carry>0:
    rev_a.append(1)
ans = list(reversed(rev_a))
while ans[0] == 0:
    ans.pop(0)
print(ans)

# print(carry, rev_a)





























#
#
#
# for i in range(n-1, -1, -1):
#     a[i] = a[i] % 10 + carry
#     print("digit: ",a[i], 'carry:', carry)
#     if a[i] == 10:
#         carry = a[i] // 10
#         a[i] = a[i] % 10
#         print('carry:', carry)
#
#
#     print(a[i])
#         # print(a[i])
