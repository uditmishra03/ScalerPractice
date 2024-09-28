import sys
A = 10
B = 1
C = [1, 8, 11, 3]

def check(arr, mid, k):
    n = len(arr)
    cur_sum =0
    painters = 1

    for i in range(n):
        if cur_sum + arr[i] <= mid:
            cur_sum += arr[i]
        else:
            cur_sum = arr[i]
            painters +=1

    if painters > k:
        return False
    else:
        return True


ans, lo, hi = sys.maxsize, max(C), sum(C)

# print(ans, lo, hi)

while lo <= hi:
    mid = (lo+hi)//2
    if check(C, mid, A)== True:
        ans = min(ans, mid)
        hi = mid -1 # go left

    else:
        lo = mid+1


print('Final ans:', ans)