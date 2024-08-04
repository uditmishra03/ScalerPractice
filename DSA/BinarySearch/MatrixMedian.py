A = [   [1, 3, 5],
        [2, 6, 9],
        [3, 6, 9],
        [4, 6, 8]   ] 


def getMedian(matrix):
    arr = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            arr.append(matrix[i][j])

    # Sort the array
    print(arr)
    arr.sort()
    print("mat after sort:", arr)

    # Find the median element
    mid = len(arr) // 2
    # print('mid: ', mid, 'len:', len(arr))
    if len(arr) % 2 == 0:
        # print("at line 21")
        median = (arr[mid-1] + arr[mid]) / 2
    else:
        # print("at line 24")
        median = arr[mid]

    return median


print(getMedian(A))