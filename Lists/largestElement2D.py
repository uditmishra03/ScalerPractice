'''Given a 2D array A of N rows and M columns. Find value of largest element in each row.
Note: The 2D array A is already passed as an argument to the function. User don't need to take any input.
Just perform the task on the passed arguments and return the required result.'''

# A = [[1, 2], [1, 3]]
A = [[1, 2, 3]]
sol = []
for i in range(len(A)):
    # print(A[i])
    max =0
    for j in range(len(A[i])):
        # print(A[i][j])
        if max < A[i][j]:
            max = A[i][j]
    sol.append(max)

print(sol)
