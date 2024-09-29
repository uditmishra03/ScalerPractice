A= [1, 4, 10]
B= [0, 1, 2, 5]

i , j = 0, 0
n, m = len(A), len(B)
result =[]

while i < n and j < m:
    if A[i] < B[j]:
        result.append(A[i])
        i+=1
    else:
        result.append(B[j])
        j+=1

# if pointer i has not reached the end.
while i <n:
    result.append(A[i])
    i+=1
while j<m:
    result.append(B[j])
    j+=1

print('Final ans:', result)