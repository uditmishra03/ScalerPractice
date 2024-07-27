import functools

def distance(x, y):
    return x*x + y*y

def compare(coord1,coord2):
    x1, y1= coord1[0], coord1[1]
    x2, y2= coord2[0], coord2[1]
    d1 = distance(x1, y1)
    d2 = distance(x2, y2)
    if d1 < d2:
        return -1
    elif d1 > d2:
        return 1
    else:
        return 0
    
# A = [ 
#        [1, 3],
#        [-2, 2] 
#      ]
# B = 1

A = [[1, -1],[2, -1]] 
B = 1

# # A= [[26,41],[40,47],[47,7],[50,34],[18,28]]
# B = 5

ans = sorted(A, key=functools.cmp_to_key(compare))
print(ans[:B])
# print(ans[B-1])
