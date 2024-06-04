# A = [4, 3, 2, 6, 1]
# B = 3
# C = 11

# A = [4, 2, 2, 5, 1]
# B = 4
# C = 6

A = [6,3,3,6,7,8,7,3,7]
B = 2
C = 10
def checkSubArraySum(A, B, C):
    ans = 0
    sum_subarr = 0
    subarrayMatches = False
    # Get the sum of 0 to k-1 elements.
    print(A[:B])
    for i in A[:B]:
        sum_subarr += i
    # ans = sum_subarr
    # print(sum_subarr)
    if sum_subarr == C:
        print('debug 23, in if condition')
        subarrayMatches = True

    start = 1
    end = B
    while end < len(A):
        sum_subarr = sum_subarr + A[end] - A[start-1]
        # print('@debug 21', sum_subarr)
        # ans = max(ans, sum_subarr)

        start +=1
        end +=1
        # print('debug at 33', ans)
        if sum_subarr == C:
            # print('debug 34, in if condition')
            subarrayMatches = True

    if subarrayMatches:
        return 1
    else:
        return 0

print(checkSubArraySum(A, B, C))


