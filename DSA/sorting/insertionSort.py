A = [5, 10, 2, 9, 3]
print(A)
n = len(A)
for i in range(1, n):
    key = A[i]
    j = i-1
    print(f"key: {key}, Array: {A}")
    while j >=0 and key < A[j]:
        print(f"j: {j}")
        A[j+1] = A[j]
        j -=1
    print(f"new j: {j}")
    A[j+1]=key
    print(f"pass {i}: {A}")
    print()
print(f"final: {A}")