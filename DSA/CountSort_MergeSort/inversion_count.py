'''Problem Description
Given an array of integers A. If i < j and A[i] > A[j], then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (109 + 7).

'''



def inversionCount(arr):
    inv_cnt =0
    if len(arr) > 1:
        mid = len(arr)//2
        arr1 = arr[:mid]
        arr2 = arr[mid:]

        # print(f"subarr1: {arr1}, subarr2: {arr2}")
        inv_cnt += inversionCount(arr1)
        inv_cnt += inversionCount(arr2)
        
        i, j, k =0, 0, 0
        n, m = len(arr1), len(arr2)
        # print('size', n, m)

        while i< n and j < m:
            if arr1[i] <= arr2[j]:
                arr[k] = arr1[i]
                i +=1
            else:
                arr[k] = arr2[j]
                inv_cnt += n-i
                j +=1
            k +=1

        # print('comparison over:', i, j)
        # if pointer i has not reached the end.
        while i < n:
            arr[k] = arr1[i]
            i+=1
            k+=1
        while j < m:
            arr[k] = arr2[j]
            j +=1
            k +=1
        # print('sorted arr: ', arr)
    return inv_cnt
    


# A = [1, 3, 2]
# A = [3, 4, 1, 2]
A =[8, 4, 2, 1]

mod = 10**9 +7

print('final ans:', inversionCount(A)% mod)