'''Problem Description
Given an array A of length N. Also given are integers B and C.

Return 1 if there exists a subarray with length B having sum C and 0 otherwise'''

# A = [4, 3, 2, 6, 1]
# B = 3
# C = 11

A = [4, 2, 2, 5, 1]
B = 4
C = 6
def checksubarray(A, B, C):
    subarrayExist = False
    for i in range(len(A)-B+1):
        # print(A[i:i+B])
        sum_subarray = sum(A[i:i+B])
        # print(sum_subarray)

        if sum_subarray == C:
                # print('Debnug')
                subarrayExist = True

    if subarrayExist:
        # print(sum_subarray)
        return 1
    else:
        return 0

print(checksubarray(A, B, C))























# # n = len(arr)
# # print(arr)
# # print(pf)
# def checkSubArraySum(arr, subarraylen, value):
#     subarrayExist = False
#     # i =0
#     print(subarraylen)
#     for i in range(0, len(arr)-subarraylen+1):
#         # sum_subarray = sum(arr[i:subarraylen])
#
#         # print(arr[i:subarraylen-1+i])#, sum_subarray)
#
#         # i +=1
#     #     if sum_subarray == value:
#     #         print('Debnug')
#     #         subarrayExist = True
#     #
#     # if subarrayExist:
#     #     print(sum_subarray)
#     #     return 1
#     # else:
#     #     return 0
#
# print(checkSubArraySum(A, B, C))




