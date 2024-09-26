from time import sleep


arr = [1, 2,3, 4, 5, 6, 7]


print('Original array:', arr)

def rotateArray(arr, start, end):
    n = end+1
    temp = arr[n-1]

    for i in range(n-2, -1, -1):
        arr[i+1] = arr[i]
        
    arr[start] = temp

    return arr

n = len(arr)
print('Rotate array:', rotateArray(arr, 0, n-1))

# k = 4

# for i in range(k):
#     arr= rotateArray(arr)

# print(arr)


