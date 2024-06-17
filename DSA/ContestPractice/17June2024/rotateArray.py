A = [1, 2, 3, 4, 5, 6]
B = 3

def reversee(arr, start, end):
    i, j = start, end
    while i < j: # 4,3,2, 1 -> 3, 4,2, 1
        arr[i], arr[j] = arr[j], arr[i]
        i +=1
        j -=1
    return arr


B = B%len(A)

# print(B)
if B == 0:
    print(A)
else:
    A = reversee(A, 0, len(A)-1 )
    print("Reverse whole array one time : ", A)
    A = reversee(A, 0, B-1)
    print("Rotate from 0 till k-1: ", A)
    A = reversee(A, B , len(A)-1)   # B =2 , 4-1 = 3
    print("Rotate from k  till n-1:",  A)
    # return A

