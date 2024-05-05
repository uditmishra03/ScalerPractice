A= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# A= [[1, 2, 3], [4, 5, 6]]
# A= [[1, 2],[3, 4] ,[5, 6]]
'''You are given input as a square NxN matrix, complete the column_sum function so that it returns the sum of each column as a list.'''

print("Original Matrix: ")
for i in range(len(A)):
     print(A[i])

row_len = len(A)
col_len = len(A[0])

# print(row_len, col_len)
sum = []
for i in range(col_len):
    addition = 0
    for j in range(row_len):
        # print(A[j][i], end =' ')
        addition+=A[j][i]
    sum.append(addition)
    # print()
print("\nColumn sum array: ")
print(sum)