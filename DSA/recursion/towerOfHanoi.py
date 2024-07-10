
# clear()
ans = []
def hanoi(n , start, end):
    '''Prints the list of steps required to move n disks from the start rod to the end rod
    >>> hanoi(2, 1,3)
    1 -> 2
    1 -> 2
    2 -> 3
    '''
    
    if n ==1:
        # print('called PM at 10')
        ans.append([n, start, end])

    else:
        other = 6-(start+end)
        hanoi(n-1, start, other)

        ans.append([n, start, end])
        hanoi(n-1, other, end)
    

    return ans



A = 2
# A=3

result=[]
print(hanoi(A, 1, 3))
# print(result)