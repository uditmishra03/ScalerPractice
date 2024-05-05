# A = [2, 0, 1]
A= [3, 1, 0, 2]
'''You are given an integer array A. Now your task is to find the inverse of A.
Now, the inverse of the array is A will be an array in which we change the
positions of the values as their indices and indices as values.

So, array A = [2, 0, 1]
- Now 2 is at index 0. So, place 0 at index 2.
- 0 is at index 1. So, place 1 at index 0.
- 1 is at index 2. So, place 2 at index 1.

So, the inverse of A will be [1, 2, 0]
Note: The integer array A is already passed as an argument to the function. User don't need to take any input. Just perform the task on the passed arguments and return the required result.
'''
B = []

for i in range(len(A)):
    if i in A:
        B.append(A.index(i))
print(B)