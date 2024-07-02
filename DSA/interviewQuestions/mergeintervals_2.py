# arr = [ [1, 3], [2, 6], [8, 10], [15, 18] ]
arr = [ [2, 10], [4, 9], [6, 7] ]
cur_start = arr[0][0]
cur_end = arr[0][1]
ans =[]

n = len(arr)

for i in range(n):
    if arr[i][0] > cur_end:
        ans.append([cur_start, cur_end])
        cur_start = arr[i][0]
        cur_end = arr[i][1]
    else:
        cur_end = max(cur_end, arr[i][1])

ans.append([cur_start, cur_end])

print(ans)