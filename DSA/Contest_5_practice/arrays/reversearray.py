arr = [1, 2,3, 4, 5, 6, 7]


def reversearray(arr, start, end):
    i, j = start, end
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i+=1
        j-=1
    
    return arr


k = 7 # rotate the array by k times.


n = len(arr)

# step 1: reverse the whole array
arr=reversearray(arr, 0, n-1)
print("reversing whole array:", arr )

# print('Chekcing: ', arr)

# step 2: reverse 0 to k-1 array
arr = reversearray(arr, 0, k-1)
print("reversing 0 to k-1: ", arr)

# print('Chekcing: ', arr)

# step 3: reverse k to n-1 array
arr = reversearray(arr, k, n-1)
print("reversing k to n-1: ", arr)



