'''Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements in both the array.

NOTE:

Each element in the result should appear as many times as it appears in both arrays.
The result can be in any order.'''


A = [1, 2, 2, 1]
B = [2, 3, 1, 2]

A = [2, 1, 4, 10]
B = [3, 6, 2, 10, 10]


    freq= {}

    for i in A:
        if i not in freq:
            freq[i] =1
        else:
            freq[i] +=1

    print(freq)
    ans  = []

    for each in B:
        if each in freq:
            freq[each] +=1
            print(freq)
            if freq[each]%2 <= 1:
                ans.append(each)
    print('final ans: ', ans)

# hs_a = set(A)
# print(hs_a)

# ans = []

# for i in B:
#     if i in hs_a:
#         ans.append(i)

