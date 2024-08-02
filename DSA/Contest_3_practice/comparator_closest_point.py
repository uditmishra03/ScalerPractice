from functools import cmp_to_key

# A= [[1,3],[-2,2]]
# B = 1

# A = [[1, -1],[2, -1]] 
# B = 1

# A= [[26,41],[40,47],[47,7],[50,34],[18,28]]
# B = 5

def calcDistance(c):
    x, y = c[0], c[1]
    return x*x + y*y

def compareDistance(c1, c2):
    f1 = calcDistance(c1)
    f2 = calcDistance(c2)

    # print(f1, f2)
    if f1 < f2:
        return -1
    elif f1> f2:
        return 1
    else:
        return 0


ans = sorted(A, key=cmp_to_key(compareDistance))

print(ans[:B])