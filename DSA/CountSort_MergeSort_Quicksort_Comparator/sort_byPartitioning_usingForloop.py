# A =[6, 2, 0, 4, 5]

A = [1, 4, 10, 2, 1, 5]


def partition(arr):
    if not arr:
        return -1
    
    n = len(arr)
    pivot = arr[-1]  # setting pivot as last element.
    begin = 0        # Pointer for the boundary of elements less than pivot.

    for index in range(n-1):
        if arr[index] < pivot:
            arr[index], arr[begin] = arr[begin], arr[index]
            begin +=1
    
    # Place the pivot at correct position.
    pivot_index = begin
    arr[pivot_index], arr[-1] = arr[-1], arr[pivot_index]

    return arr, pivot_index


print(partition(A))


