'''Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.

Note: A linear time complexity is expected and you should avoid use of any library function.'''

# A = [4, 7, 9]
# B = [2, 11, 19]

# A = [1]
# B = [2]
# A = [-4,-3,0]
# B = [2]
A = [3]
B = [-4,-3]

def merge2Arrays(arr1, arr2):
    i, j =0, 0
    n, m = len(arr1), len(arr2)
    # print('size', n, m)

    result = []

    while i< n and j < m:
        # print(i, j)
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i +=1
        else:
            result.append(arr2[j])
            j +=1
        # print('intermediate result:', result)

    # print('comparison over:', i, j)
    # if pointer i has not reached the end.
    while i < n:
        result.append(arr1[i])
        i+=1
    # if pointer j has not reached the end.
    while j < m:
        result.append(arr2[j])
        j +=1
    
    return result




print(merge2Arrays(A, B))