'''You are given an array A of N elements. Find the number of triplets i,j and k such that i<j<k and A[i]<A[j]<A[k]'''

A = [1, 2, 4, 3]
n = len(A)
count = 1
for i in range(1, n-1):
    foundLeft, foundRight = False, False
    print( A[i-1], A[i], A[i+1])
    left, right = i-1, i+1
    while left > 0:
        if A[left] < A[i]:
            foundLeft = True
            # break
        # else:
        left -=1
        print(f"left: {left}")
    while right > n:
        if A[right] > A[i]:
            foundRight = True
            # break
        # else:
        right +=1
        print(f"right: {right}")
    print('@line 23', foundRight, foundLeft)
    if foundLeft ==True and foundRight == True:
        print( 'Triplets:', A[i-1], A[i], A[i+1])
        count +=1
print(count)
