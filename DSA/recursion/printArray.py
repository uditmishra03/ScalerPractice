A = [6, -2, 5, 3]
n = len(A)
# print(n)


def printElements(arr, cur_idx=0):

    n = len(arr)
    # print('length of array: ', n, 'and current index: ', cur_idx)
    # cur_idx = 0
    if cur_idx == n:
        return
    print(arr[cur_idx], end =' ')
    printElements(arr, cur_idx+1)
    


printElements(A)
print()