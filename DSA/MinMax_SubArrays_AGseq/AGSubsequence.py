"""Problem Description
You have given a string A having Uppercase English letters.

You have to find the number of pairs (i, j) such that A[i] = 'A', A[j] = 'G' and i < j."""

'''
1. Run a loop from 0 to n-1, init count_a and ans as 0

1a. This checks for each char in the sequence, 
1b. if 'a' is found then count_a is incremented.
1b. if 'g' is found then ans = ans + count_a
'''
# A = "ABCGAG"
# A = "GAB"
A = "BACGGDEGAG"
count_a, ans = 0, 0

for i in A:
    # print(i)
    if i == 'A':
        count_a +=1
    if i == 'G':
        ans = ans + count_a
    print(i, count_a, ans)
print("ans= ", ans)