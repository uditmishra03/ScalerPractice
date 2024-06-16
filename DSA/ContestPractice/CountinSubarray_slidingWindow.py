'''Problem Description
Given an array A of N non-negative numbers and a non-negative number B,
you need to find the number of subarrays in A with a sum less than B.
We may assume that there is no overflow.'''
#
# A = [2, 5, 6]
# B = 10
A = [1, 11, 2, 3, 15]
B = 10

n = len(A)
start, end, count = 0, 0, 0
sum = A[0]

'''1. keep a track of start and end, should not go beyound the len of Array.
2. check the sum, if smaller than B: 
2a. then increment end by 1.
2b. check if start is less than end, if yes then
add the length of array ie. end -start to count
2c. add the value of end (new one) to sum.
3. else ie. sum is not smaller than B:
3a. from the sum, subtract the start element
3b. then. move start ahead, ie. increment by 1
'''
while start <n and end < n:
    if sum < B:
        end +=1
        if start <= end:
            count += end -start
        if end < n:    # checking this again because after entering while we are incrementing end again, which may result the value to go out of bound.
            sum += A[end]
    else:
        sum -= A[start]
        start +=1

print(count)