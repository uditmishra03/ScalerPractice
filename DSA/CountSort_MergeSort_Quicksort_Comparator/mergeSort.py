'''Given an integer array A, sort the array using Merge Sort.'''

A = [1, 4, 10, 2, 1, 5]


print('Original array: ', A)
print()
def mergeSort(arr):

    if len(arr) > 1:
        mid = len(arr)//2
        arr1 = arr[:mid]
        arr2 = arr[mid:]

        # print(f"subarr1: {arr1}, subarr2: {arr2}")
        mergeSort(arr1)
        mergeSort(arr2)
        
        i, j, k =0, 0, 0
        n, m = len(arr1), len(arr2)
        # print('size', n, m)

        while i< n and j < m:
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i +=1
            else:
                arr[k] = arr2[j]
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
            k+=1
        return arr
    
print('final ans:', mergeSort(A))
