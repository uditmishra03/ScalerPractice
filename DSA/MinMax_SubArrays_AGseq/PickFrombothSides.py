'''Problem Description
You are given an integer array A of size N.

You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.

Find and return the maximum possible sum of the B elements that were removed after the B operations.

NOTE: Suppose B = 3, and array A contains 10 elements, then you can:

Remove 3 elements from front and 0 elements from the back, OR
Remove 2 elements from front and 1 element from the back, OR
Remove 1 element from front and 2 elements from the back, OR
Remove 0 elements from front and 3 elements from the back.'''

# A = [5, -2, 3 , 1, 2]
# B = 3
A = [2, 3, -1, 4, 2, 1]
B = 4

finSum = 0
def SumofArray(arr):
    s =0
    for each in arr:
        s +=each
    return s

start = 0
end = len(A)-1
print(A)
for i in range(B, 0, -1):
    print(start, end)
    print("i: ",  i,'|', A[start:i], SumofArray(A[start:i]), '|',  A[-i:], SumofArray(A[-i:]))
    if SumofArray(A[start:i]) >= SumofArray(A[-i:end ]):
        finSum += A[start]
        # finSum += A.pop(0)
        start += 1
        print('from front, final sum: ', finSum)
        # print('New array: ', A)
    else:
        finSum += A[end]
        # finSum += A.pop(-1)
        end -= 1
        print('from back, final sum: ', finSum)
        # print('New array: ', A)


print(finSum)