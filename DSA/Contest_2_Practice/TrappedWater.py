arr = [2, 1, 3, 2, 1, 2, 4, 3, 2, 1, 3, 1]

'''
1. Find Lmax for the arr
lmax[i] = max(lmax[i-1], arr[i])
1. Find Rmax for the arr ( from n-2 to 0)
rmax[i] = max(rmax[i+1], arr[i])

3.
set water as zero.
4, 
run a loop from 1 to n-2.
left_sup = lmax[i-1]
right_sup = rmax[i+1]

net_support = min(left_sup, right_sup)

if arr[i] < net_support:
water = water + (net_support-arr[i])

5. return water as answer.
'''


n = len(arr)
lmax =[0]*n
lmax[0] = arr[0]
for i in range(1, n):
    lmax[i] = max(lmax[i-1], arr[i])

# print(lmax)

rmax =[0]*n
rmax[n-1] = arr[n-1]
for i in range(n-2, -1, -1):
    rmax[i] = max(rmax[i+1], arr[i])

# print(rmax)

water = 0

for i in range(1, n-2):
    left_sup = lmax[i-1]
    right_sup = rmax[i+1]

    net_support = min(left_sup, right_sup)
    if arr[i] < net_support:
        water = water + (net_support-arr[i])


print('final ans:', water)
    