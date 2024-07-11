'''Problem Description
You have given a string A having Uppercase English letters.
You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j.'''

# A = "ABCGAG"
A = "GAB"

count_of_a , ans = 0, 0
for i in A:
    if i == 'A':
        count_of_a +=1
    elif i =='G':
        ans = ans + count_of_a

print(ans)