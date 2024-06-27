'''Problem Description

Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.

Note: It is possible to swap any two elements, not necessarily consecutive.'''
import sys

A = [5, 17, 100, 11]
B = 20

# A = [1, 12, 10, 3, 14, 10, 5]
# B = 8
# A= [52,7,93,47,68,26,51,44,5,41,88,19,78,38,17,13,24,74,92,5,84,27,48,49,37,59,3,56,79,26,55,60,16,83,63,40,55,9,96,29,7,22,27,74,78,38,11,65,29,52,36,21,94,46,52,47,87,33,87,70]
# B =  19


def findMinSwaps(A, B):
    answer = sys.maxsize
    smallElements = 0
    for i in A:
        if i <= B:
            smallElements +=1

    print('Window size: ', smallElements)

    badElements = 0

    for i in range(smallElements):
        if A[i] > B:
            badElements +=1

    print(f"BadElements in first window: {badElements}")
    answer = min(answer, badElements)
    print(f"answer so far: {answer}")

    start, end =1, smallElements

    while end < len(A):
        print(A[start:end+1])
        if A[start-1] > B:
            badElements -=1
        if A[end] > B:
            badElements +=1
        start +=1
        end +=1
        answer = min(answer, badElements)

    return answer

print(findMinSwaps(A, B))