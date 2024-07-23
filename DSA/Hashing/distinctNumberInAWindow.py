'''You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.

Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

NOTE: if B > N, return an empty array.'''

from collections import defaultdict


A = [1, 2, 1, 3, 4, 3]
B = 3


# A = [1, 1, 2, 2]
# B = 1

def findDistinctNumbers(arr, window):
    n = len(arr)
    # print('original array: ', arr)
    # print('max len of array:', n)
    ans = []
    if window > n:
        return ans
    
    freq_arr = defaultdict(int)
    for i in range(window):
        freq_arr[arr[i]] +=1
    # print('freq array: ', freq_arr,'\ndistinct elements count : ',  len(freq_arr))
    ans.append(len(freq_arr))

    print()
    start ,end = 1, window
    while end < n:
        # print("Window: ", start+1)
        # print(f"start: {start}, end:{end}")
        # print(f"Outgoing: {arr[start-1]}, \nIncoming: {arr[end]}")
        freq_arr[arr[end]] +=1
        freq_arr[arr[start-1]] -=1
        
        if freq_arr[arr[start-1]] == 0:
            freq_arr.pop(arr[start -1])
        # print(freq_arr)
        ans.append(len(freq_arr))
        # print(f"unq elements in this window: {len(freq_arr)}")
        start +=1
        end +=1
        
        # print()

    return ans


print(findDistinctNumbers(A, B))