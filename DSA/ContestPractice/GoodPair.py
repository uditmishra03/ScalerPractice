'''Problem Description
Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.'''

A = [1,2,2]
B = 4
# A = [1,2,4]
# B = 4
# # A = [1,2,3,4]
# # B = 7

n = len(A)
goodpairExist = False
for i in range(n):
    for j in range(i+1, n):
        if A[i] + A[j] ==B:
            goodpairExist = True
            print(f"1, Good pair i.e., {A[i], A[j]} exist.")
            break
    if goodpairExist:
        break
if not goodpairExist:
    print("Good pair does not exist.")