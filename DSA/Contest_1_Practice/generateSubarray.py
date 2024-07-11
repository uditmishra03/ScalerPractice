
# Input 1:
# A = [1, 2, 3]
# Input 2:
A = [5, 2, 1, 4]

subarray_count = 0
for i in range(len(A)):
    # print(i, A[i])
    for j in range(i+1, len(A)+1):
        # print(i, j)
        subarray_count +=1
        print(A[i:j])

print(subarray_count)