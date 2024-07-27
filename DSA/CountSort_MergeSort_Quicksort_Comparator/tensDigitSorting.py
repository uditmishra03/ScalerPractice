import functools


# A = [15, 11, 7, 19]

A = [2, 24, 22, 19]

def findTensDigit(num):
    ans = num //10 %10
    return ans


def compare(n1, n2):
    t1 = findTensDigit(n1)
    t2 = findTensDigit(n2)
    print(t1, t2)
    if t1 < t2:
        return -1
    elif t1>t2:
        return 1
    else:                 # In case t1 == t2
        if n1 < n2:         
            return 1
        elif n1 > n2:
            return -1
        else:
            return 0
        

ans = sorted(A, key=functools.cmp_to_key(compare))

print(ans)