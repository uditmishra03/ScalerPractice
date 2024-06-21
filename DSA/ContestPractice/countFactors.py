import math

A = 12
count = 0
print('root:', int(math.sqrt(A)))
for i in range(1, int(math.sqrt(A) + 1)):
    if A % i == 0:
        print(i)
        print('line 8:', A//i)
        if i*i != A :
            print('this oen')
            count += 2
        else:
            count += 1

print('count:', count)