A = [2, 4, 3, 2]
B = 3  

# A = [1, 5, 7, 3, 2]
# B = 9

def findKthSmallest(A, B):
    n = len(A)

    triplet_sum = []

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                triplet_sum.append(A[i]+A[j]+A[k])


    print(triplet_sum)
    print("After sorting: ")
    triplet_sum.sort()

    print(triplet_sum)

    m = len(triplet_sum)
    lo, hi = 0, m-1
    while lo <= hi:
        mid = (lo+hi)//2
        # print('mid:', mid)
        if mid == B:
            return triplet_sum[mid-1]
        elif mid < B:
            lo= mid+1
        else:
            hi = mid-1


print(findKthSmallest(A, B))

