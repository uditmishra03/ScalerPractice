# Selection Sort

'''Problem Description
Find the Bth smallest element in given array A .
NOTE: Users should try to solve it in less than equal to B swaps.'''

A = [2, 1, 4, 3, 2]
B = 3
# A = [8,16,80,55,32,8,38,40,65,18,15,45,50,38,54,52,23,74,81,42,28,16,66,35,91,36,44,9,85,58,59,49,75,20,87,60,17,11,39,62,20,17,46,26,81,92]
# B = 9

print('unsorted Array: ', A)
swapCount = 0
for i in range(len(A)):
    print('Pointer is at index: ', i)
    small_index_val = i
    for j in range(i+1, len(A)):
        if A[j] < A[small_index_val]:
            small_index_val = j
    print(f"Swapping {A[i]} at index {i},  {A[small_index_val]} at index {small_index_val}")
    if A[small_index_val] != A[i]:
        A[i],  A[small_index_val] = A[small_index_val], A[i]
        swapCount += 1
    print(f"{i+1} run: {A}, swap count: {swapCount}")
    print()

print('sorted Array: ', A)
print(A[B])