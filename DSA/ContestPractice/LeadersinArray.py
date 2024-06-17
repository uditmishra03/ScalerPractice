'''Problem Description
Given an integer array A containing N distinct integers, you have to find all the leaders in array A. An element is a leader if it is strictly greater than all the elements to its right side.'''

A = [16, 17, 4, 3, 5, 2]
n = len(A)
# print(A[n-1], A[-1])

max = A[-1]
results = []
results.append(max)

for each in A[-2::-1]:
    print(f"each: {each}, max ={max}" )
    if max < each:
        max = each
        results.append(each)
print(results)
