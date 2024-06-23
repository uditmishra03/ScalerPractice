'''Problem Description
Given a number A, find if it is COLORFUL number or not.

If number A is a COLORFUL number return 1 else, return 0.

What is a COLORFUL Number:

A number can be broken into different consecutive sequence of digits.
The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245.
This number is a COLORFUL number, since the product of every consecutive sequence of digits is different'''


def findproductOfDigits(num):
    # num = 23
    product = 1
    original_num = num
    while num > 0:
        rem = num % 10
        product *=rem
        num = num //10
    return product

A = 3245
a = str(A)
# print(a, type(a))
n = len(a)
subsequence_A = []
for i in range(len(a)):
    for j in range(i, n):
        # print(a[i:j+1], type(a[i:j+1]))
        subsequence_A.append(int(a[i:j+1]))

print(subsequence_A)
prodOfdigits = []
for each in subsequence_A:
    prod = findproductOfDigits(each)
    print(f"num: {each}, prod: {prod}")
    if prod not in prodOfdigits:
        prodOfdigits.append(prod)
        colorfulNumber = True
        print(f"{A} is a coloful number, return 1")
    else:
        print("already exist, return 0")

if colorfulNumber:
    print('Return 1')
# print(original_num, product)

