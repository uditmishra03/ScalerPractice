arr = [1, 2, 3, 5, 1, 3, 5, 9, 2]

ans = 0
for i in range(len(arr)):
    ans ^=arr[i]

print('Final ans: ', ans) 