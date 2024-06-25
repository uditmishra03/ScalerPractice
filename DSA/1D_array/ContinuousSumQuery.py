'''Problem Description
There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next to each other.

Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, given by the 2D array B'''


A = 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

beggers = [0]*A

for i in range(len(B)):
    # print(B[i])
    left = B[i][0]-1
    right = B[i][1]-1
    value = B[i][2]
    print('left:', left,'right: ', right, 'value:', value)
    beggers[left] += value
    if right+1 < A:
        print('~~~Subtracting', value,'from index: ', right+1)
        beggers[right+1] -= value
print(beggers)

prefixsum = [0]*A
prefixsum[0]= beggers[0]
for i in range(1, A):
    prefixsum[i] = prefixsum[i-1] + beggers[i]

print(prefixsum)