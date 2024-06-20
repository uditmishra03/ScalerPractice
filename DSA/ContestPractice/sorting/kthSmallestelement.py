A = [2, 1, 4, 3, 2]
B = 3

print("Original array: ", A)

for i in range(B):
    smallest_val_idx = i
    for j in range(i+1, len(A)):
        if A[j] < A[smallest_val_idx]:
            smallest_val_idx = j

    if A[i] != A[smallest_val_idx]:
        print(f"Swapping {A[i], A[smallest_val_idx]}")
        A[i], A[smallest_val_idx] = A[smallest_val_idx], A[i]
    else:
        print('no swapping')
    print(f"Pass {i}: {A}")

print(A[B-1])