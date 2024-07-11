# A = [-2, 1, -4, 5, 3]
A = [1, 3, 4, 1]

max_val, min_val = A[0], A[0]

for val in A:
    if max_val < val:
        max_val = val
    if min_val > val:
        min_val = val

print(f"max: {max_val}, min: {min_val}")

print(max_val+min_val)