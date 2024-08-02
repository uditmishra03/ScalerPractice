import functools
import math
# num = 12

def countFactor(num):
    count = 0
    for i in range(1, int(math.sqrt(num))+1):
        # print('checking for:', i)
        if num % i == 0:
            if i*i != num:
                count +=2
            else:
                count +=1
    return count
    # factors.append(i)

# print(countFactor(num))

# A = [6, 8, 9]
A = [2, 4, 7]

def compare(n1, n2):
    f1 = countFactor(n1)
    f2 = countFactor(n2)

    if f1 < f2:
        return -1
    elif f1 > f2:
        return 1
    else:
        if n1 < n2:
            return -1
        elif n1 > n2:
            return 1
        else:
            return 0
        

ans = sorted(A, key=functools.cmp_to_key(compare))

print(ans)