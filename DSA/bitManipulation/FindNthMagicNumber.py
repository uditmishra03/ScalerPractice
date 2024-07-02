'''Problem Description
Given an integer A, find and return the Ath magic number.

A magic number is defined as a number that can be expressed as a power of 5 or a sum of unique powers of 5.

First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….'''

A = 10
power = 5
ans = 0
while A > 0:
    remainder = A %2
    A = A//2
    value = remainder * power
    print(value)
    ans += value
    power *= 5
    # print(ans)
print(ans)