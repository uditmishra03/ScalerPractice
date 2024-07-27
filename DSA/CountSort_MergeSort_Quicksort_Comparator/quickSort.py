'''Given an integer array A, sort the array using Quick Sort.
'''
import sys
sys.setrecursionlimit(1500)

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
    print('at line 24:', pivot_index)
    return pivot_index+1



def quicksort(arr, start, end):
    # print(f'arr: {arr}'(), start: {start}, end: {end}')
    # if start == end:
    #     return
    if start < end:
        pivotIndex = partition(arr)
        # print('at line 34:: pivot_index', pivotIndex)
        quicksort(arr, start, pivotIndex-1)
        quicksort(arr, pivotIndex+1, end)
        # print(arr)
        # return arr


start = 0
n = len(A)
print('Original array: ', A)
quicksort(A,start=0, end=n-1)


