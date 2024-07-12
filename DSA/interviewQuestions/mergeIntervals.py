'''Problem Description
You have a set of non-overlapping intervals. You are given a new interval [start, end], insert this new interval into the set of intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.'''

arr =[ [1, 3], [6, 9] ]
interval = [2, 5]
# arr = [[1, 3], [6, 9]]
# interval = [2, 6]
n = len(arr)


ans = []

for i in range(0, n):
    print('end', arr[i][1], 'start', interval[0])
    print(arr[i][1], interval[1])
    if arr[i][1] < interval[0]:
        print('inside iff condition @line 19')
        ans.append(arr[i])

    elif arr[i][0] > interval[1]:
        print('inside iff condition @line 23')
        ans.append(interval)
        for j in range(i, n):
            ans.append(arr[j])
        break
    else:
        print('inside else condition @line 29')
        interval[0] = min(interval[0], arr[i][0])
        interval[1] = max(interval[1], arr[i][1])

# ans.append(interval)

print(ans)