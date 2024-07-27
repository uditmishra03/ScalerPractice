'''Problem Description
Given an array A of non-negative integers, arrange them such that they form the largest number.

Note: The result may be very large, so you need to return a string instead of an integer'''
import functools

# A = [2, 3, 9, 0]
# A = [0,0,0,0,0]
A = [3,30,34,5,9]

def compareNumbers(x, y):
    str1 = str(x)
    str2 = str(y)
    if str1+str2 > str2+str1:
        return -1
    else:
        return 1


def largestNumber(A):

    ans = sorted(A, key=functools.cmp_to_key(compareNumbers))

    # print(ans)
    result = ''.join(map(str, ans))
    # print(result)

    # Handle the case where all numbers are zero
    if result[0] == '0':
        return '0'

    return result


print(largestNumber(A))