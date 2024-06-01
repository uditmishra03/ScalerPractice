"""Problem Description
You are given an array A of N integers.
Return a 2D array consisting of all the subarrays of the array

Note : The order of the subarrays in the resulting 2D array does not matter."""

# nput 1:
# A = [1, 2, 3]


# Input 2:
A = [5, 2, 1, 4]
# A= [36,63,63,26,87,28,77,93,7]

def genSubarray(arr):
    print(len(arr))
    subarray = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)+1):
            subarray.append(arr[i:j])
    print(len(subarray))
    return subarray


print(genSubarray(A))
