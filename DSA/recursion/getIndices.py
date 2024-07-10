'''Problem Description
Given an array of integers A with N elements and a target integer B, the task is to find all the indices at which B occurs in the array.'''

# A = [1, 2, 3, 4, 5]
# B = 1

A = [8, 9, 5, 6, 5, 5]
B = 5




def findIndex(arr, B, cur_idx, result):
    print("current index is: ", cur_idx)
    n = len(arr)
    if cur_idx == n:
        return
    if arr[cur_idx] == B:
        result.append(cur_idx)
    # print(result)
    findIndex(arr, B, cur_idx+1, result)
    return result

ans = []
findIndex(A, B, 0, ans)
print("final ans:", ans)
