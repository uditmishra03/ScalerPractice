'''Problem Description
You are given an integer array C of size A. Now you need to find a subarray (contiguous elements) so that the sum of contiguous elements is maximum.
But the sum must not exceed B.'''

A = 5 # size
B = 12 # maxVal
C = [2, 1, 3, 4, 5] #array
# print(C)

start, end, i = 0, 0, 0
ans = 0
sum = 0
# sum = C[0]
for start in range(A):
    sum = 0
    for end in range(start, A):
        # sum = sum + C[end]
        # print(f"debug @14: start: {start}, end : {end}, sum :{sum}")

        if sum <= B:
            sum = sum + C[end]
            ans = max(sum, B)
            #
            # print(f"sum = {sum}, added element: {C[end]}")
        else:
            # break
            start +=1
            sum = sum - C[start]
            ans = max(sum, B)
            # print(f"sum = {sum}, subtracted element: {C[start]}")

print(ans)

