arr = [1, 2, 0]
# arr = [2,3,1,2]
# arr = [3, 4, -1, 1]
# arr = [-8, -7, -6]
n = len(arr)
print(n, n+2)


for i in range(n):
    if arr[i] <=0:
        arr[i] = n+2

print("updated array", arr)


# Marking each element.

for i in range(n):
    ele = abs(arr[i])
    idx = ele-1
    if 0<= idx < n  and arr[idx] > 0:
        arr[idx] = arr[idx] * -1
        print(arr)

print("array after marking the indexes", arr)

for i in range(n):
    if arr[i] > 0:
        print('ans:', i+1)
        break
    else:
        print(n+1)