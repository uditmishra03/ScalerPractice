'''Problem Description
Given an array of integers A and an integer B, find and return the minimum number of swaps required to bring all the numbers less than or equal to B together.
Note: It is possible to swap any two elements, not necessarily consecutive.'''

# A = [1, 12, 10, 3, 14, 10, 5]
# # A = [1, 12, 10, 3, 14, 10, 5,4, 6]
# B = 8
A = [5, 17, 100, 11]
B = 20
# print(A)
lesserIndex = []
smallerNocount =0
for i in range (len(A)):
    if A[i] <= B:
        lesserIndex.append(i)
        smallerNocount +=1
# print(lesserIndex, smallerNocount)

largernoCount =0
for i in range(0, smallerNocount):
    # print(A[i])
    if A[i] > B:
        largernoCount +=1

minSwaps = largernoCount


start =1
end = smallerNocount

while end < len(A):
    # print('sliding window:', 's_idx:', start,'e_idx:',  end, A[start:end+1])
    # print('Gone ele:', A[start-1], 'coming ele:', A[end])
    if A[start-1] > B:
        largernoCount -=1
    if A[end] > B:
        largernoCount +=1

    # print('largecount:', largernoCount, '\n')
    if minSwaps > largernoCount:
        minSwaps = largernoCount
    start += 1
    end += 1
print(minSwaps)