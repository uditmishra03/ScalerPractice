'''Problem Description
Given a number A, find if it is COLORFUL number or not.

If number A is a COLORFUL number return 1 else, return 0.

What is a COLORFUL Number:

A number can be broken into different consecutive sequence of digits.
The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245.
This number is a COLORFUL number, since the product of every consecutive sequence of digits is different'''

A = 235
numbers = []
while A > 0:
    num = A % 10
    numbers.append(num)
    A = A//10
    # print(A)
numbers.reverse()
print(numbers)
n = len(numbers)
subseq = []
for i in range(n):
    for j in range(i+1, n+1):
        subseq.append(numbers[i:j])
print(subseq)

final_subseq =[]

print(final_subseq)