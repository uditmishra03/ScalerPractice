# A = [5, 17, 100, 11]
# B = 2

A = [1, 2, 3, 4, 5]
B = 3

print('Original array:', A)
queue = []

for i in range(B-1, -1, -1):
    queue.append(A[i])

# print(queue)

for i in range(B-1, -1, -1):
    A[i]= queue.pop()

print(A)