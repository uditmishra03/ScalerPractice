'''Problem Description
Farmer John has built a new long barn with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall and an integer B which represents the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?'''

# A = [1, 2, 3, 4, 5]
# B = 3

# A = [1, 2]
# B = 2

A = [5,17,100,11]
B = 2


def check(arr,mid, k):
    n = len(arr)
    count = 1
    prev_cow = arr[0]
    for i in range(1, n):
        if (arr[i] - prev_cow) >= mid:
            count +=1
            prev_cow = arr[i]
    if count >= k:
        return True
    else:
        return False

def aggressiveCows(arr, k):
    n = len(arr)
    # print(arr)
    arr.sort()
    # print(arr)
    lo,hi = 1, arr[n-1] - arr[0]

    while lo <= hi:
        mid = (lo+hi)//2
        if check(arr, mid, k) == True:
            ans = mid
            lo = mid+1
        else:
            hi = mid-1
    
    return ans


print(aggressiveCows(A, B))