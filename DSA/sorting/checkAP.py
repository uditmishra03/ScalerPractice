'''Problem Description
Given an integer array A of size N. Return 1 if the array can be arranged to form an arithmetic progression, otherwise return 0.
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.'''

# Input 1:
A = [3, 5, 1]
# Input 2:
# A = [2, 4, 1]
# A = [-113, -70, -14, -8, -29, 5, -94, -44, 23, 9, 13, -132, -14]


def checkAP(arr):
    arr.sort()
    print(arr)
    equal_diff = True
    diff = arr[1] - arr[0]
    # print(diff)
    for i in range(1, len(arr)-1):
        # print(arr[i] - arr[i - 1] , arr[i + 1] - arr[i])
        if diff != arr[i + 1] - arr[i]:
            equal_diff = False
            # print(diff, arr[i+1]-arr[i])

    if equal_diff:
        return 1
    else:
        return 0


print('result :' , checkAP(A))