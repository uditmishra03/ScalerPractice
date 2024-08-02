from functools import cmp_to_key  as cmp
# A = [6, 8, 9]
# A = [2, 4, 7]

A = [9, 3, 10, 6, 4 ]


def calcFactors(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            # print(i)
            count +=1
    return count

# print('count:', calcFactors(18))


def sortByFactors(a, b):
    f1 = calcFactors(a)
    f2 = calcFactors(b)
    # print(f1, f2)

    if f1 < f2:
        return -1
    elif f1 > f2:
        return 1
    else:
        if a < b:
            return -1
        elif a > b:
            return 1
        else: 
            return 0
    

ans = sorted(A, key=cmp(sortByFactors))

print(ans)