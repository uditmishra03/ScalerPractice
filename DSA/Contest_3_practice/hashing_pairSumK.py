'''Given arr[N] and K, check if there exists a pair (i, j) such that arr[i] + arr[j] == K && i != j.'''

arr = [8 ,9 ,1 ,-2, 4, 5, 11, -6, 4]
k =8

freq= {}
count = 0
for i in arr:
    target = k - i
    if target in freq:
        print('yes', target, i)
        break
        count = freq[target]
    else:
        freq[i] = 1
    
    print(freq)

print('final ans:', count)