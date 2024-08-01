from collections import defaultdict

# A = [3, 5, 1, 2]
# B = 4

A = [1, 2, 1, 2]
B = 1

freq = defaultdict(int)
count = 0
for i in range(len(A)):
    diff_target = A[i] -B
    sum_target = A[i] + B
    print('for ', A[i], '--> ', diff_target, sum_target)

    if diff_target in freq:
        count += freq[diff_target]

    
    if sum_target in freq:
        count += freq[sum_target]

    freq[A[i]] +=1

    print(freq)
    print('intermeidate ans:', count)
    print()

print('final ans:', count)