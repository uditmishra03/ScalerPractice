n = 6


def checkbit(N, i):
    if N & 1<<i == 0:
        return False
    else:
        return True
    
def unsetBit(N, i):
    if checkbit(N, i)== False:
        N = N^ 1<<i
    print(N)
    return N


print('Final ans:', unsetBit(2, 2))