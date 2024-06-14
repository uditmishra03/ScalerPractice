arr = [10, 32, 6, 12, 20, 1]

for i in range(1, len(arr)):
    arr[i] = arr[i-1] + arr[i]

print('prefix sum: ', arr)