from functools import cmp_to_key

# A = [2, 24, 22, 19]
A = [15, 11, 7, 19]

def findTensDigit(n):
    ans = n //10 %10
    return ans

def compareTens(n1, n2):
    t1 = findTensDigit(n1)
    t2 = findTensDigit(n2)

    if t1 < t2:
        return -1
    elif t1 > t2:
        return 1
    else:
        if n1 < n2:
            return 1
        elif n1 > n2:
            return -1
        else:
            return 0
        

result = sorted(A, key=cmp_to_key(compareTens))

print(result)