'''Given an array A. Sort this array using Count Sort Algorithm and return the sorted array.
'''

# A = [4, 2, 1, 3]
# A= [1, 3, 1]
A =[10,9,8]

def countSort(A):
    max_item = max(A)
    # print(max_item)
    farr = [0]*(max_item+1)
    for i in A:
        farr[i] +=1
    
    # print(farr)
    ans = []
    for k in range(max_item+1):
        for i in range(1, farr[k]+1):
            ans.append(k)
    return ans



print(countSort(A))