'''Problem Description
You are given an array A of N integers.
Return a 2D array consisting of all the subarrays of the array

Note : The order of the subarrays in the resulting 2D array does not matter.
'''

# A = [5, 2, 1, 4]
A = [1, 2, 3]

results = []
for i in range(len(A)):
    # print(i)
    for j in range(i+1, len(A)):
        results.append(A[i:j])

print(results)