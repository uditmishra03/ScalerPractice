'''Problem Description
Farmer John has built a new long barn with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall and an integer B which represents the number of cows.

His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?'''
import sys

# A = [1, 2, 3, 4, 5]
# B = 3

# A = [1, 2]
# B = 2

A = [5,17,100,11]
B = 2

A.sort()
# print(A)

n = len(A)

def check(arr, k, mid):
    cow_count = 1
    prev_cow_at = arr[0]

    for i in range(1, len(arr)):
        if arr[i] - prev_cow_at >= mid:
            cow_count +=1
            prev_cow_at = arr[i]

    if cow_count >= k:
        return True
    else:
        return False


min_dist = sys.maxsize
for i in range(1, len(A)):
    if A[i]-A[i-1]< min_dist:
        min_dist = A[i]-A[i-1]

# print(min_dist)

lo , hi = min_dist, A[n-1]-A[0]

ans = 0
while lo <= hi:
    mid = (lo+hi)//2
    print(mid)
    if check(A, B, mid)==True:
        ans = mid
        lo = mid+1
    else:
        hi = mid-1

print('Final ans: ', ans)

