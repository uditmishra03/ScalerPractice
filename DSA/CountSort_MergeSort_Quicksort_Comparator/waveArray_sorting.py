# A = [1, 2, 3, 4]
# A = [5,1,3,2,4]
A  = [10, 90, 49, 2, 1, 5, 23]

# A = [1, 2]

print(A)
def waveArray(arr):
    n = len(arr)
    # Traverse all even elements
    for i in range(0, n - 1, 2):
        print('value of i:', i)

        # If current even element is smaller than previous
        if (i > 0 and arr[i] < arr[i-1]):
            arr[i], arr[i-1] = arr[i-1], arr[i]
            print('@line 12:', arr)

        # If current even element is smaller than next
        if (i < n-1 and arr[i] < arr[i+1]):
            arr[i], arr[i+1] = arr[i+1], arr[i]
            print('@line 17', arr)


    print('\nfinal ans:', arr)

waveArray(A)