'''Problem Description
An integer is given to you in the form of an array, with each element being a separate digit.

Find the smallest number (leading zeroes are allowed) that can be formed by rearranging the digits of the given number in an array. Return the smallest number in the form an array.

Note - Do not use any sorting algorithm or library's sort method.'''

# A = [6, 3, 4, 2, 7, 2, 1]
A = [4,2,7,3,9,0]


def smallestNumber(A):
    n = len(A)
    print(f"Original array     :{A}")
    print(f'size               :{n}')
    freq_arr= [0]*10
    print(f'Initial freq arr   :{freq_arr}')
    for i in range(n):
        freq_arr[A[i]] +=1
    print(f'Resultant freq arr :{freq_arr}')

    # print the sorted number in the form of an array.
    result = []
    for k in range(10):
        for i in range(1, freq_arr[k]+1):
            # print(k)
            result.append(k)

    return result



print('Final ans          :', smallestNumber(A), sep='')