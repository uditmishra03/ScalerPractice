'''Problem Description
You are given an integer A, print 1 to A using using recursion.

Note :- After printing all the numbers from 1 to A, print a new line.'''

A = 9

def printNumbers(n):
    if n == 0:
        # print(1, end =' ')
        return 
    printNumbers(n-1)
    print(n, end =' ')




print(printNumbers(A))
print()