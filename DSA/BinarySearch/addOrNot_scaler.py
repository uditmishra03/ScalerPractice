

def check(count, B, A, i):
    global prefix
    if A[i] * count - (prefix[i+1] - prefix[i-count+1]) <= B:
        return True
    return False

A = [3, 1, 2, 2, 1]
B = 3

# A = [5, 5, 5]
# B = 3

# A = [-5,6,1,-5,1,-3,1,3,1,5]
# B = 9 
def solve(A, B):
    A.sort()
    print(A)
    n = len(A)

    prefix = [0] * n
    # print(prefix)
    prefix[0] = A[0]

    for i in range(1, n):
        prefix[i] = prefix[i-1] + A[i]

    print(prefix)

    ans = [-1, -1]

    for i in range(n):
        lo, hi = i, i+1
        while lo <= hi:
            count = (lo+hi)//2
            if check(count, B, A, i):
                mx = count
                lo = count +1
            else:
                hi = count -1
        if ans[0] < mx:
            ans[0] = mx
            ans[1] = A[i]
        
        return ans

    
print(solve(A, B))