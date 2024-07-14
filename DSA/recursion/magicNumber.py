'''
Given a number A, check if it is a magic number or not.

A number is said to be a magic number if the sum of its digits is calculated till a single digit recursively by adding the sum of the digits after every addition. If the single digit comes out to be 1, then the number is a magic number.'''

def sumOfdigits(A):
    if A == 1:
        return 1
    elif A < 10 and A > 1:
        return 0
    sum =0 
    while A > 0:
        sum += A %10
        A = A//10
        print(f"sum: {sum}, number: {A}")
    return sumOfdigits(sum)

A =83557

print('Original number', A)
print(sumOfdigits(A))

