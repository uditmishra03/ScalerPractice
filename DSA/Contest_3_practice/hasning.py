# A = 'banana'
# A = 'dccbcdaac'
# A = 'abcabc'
A= 'abdaccc'

from collections import defaultdict

freq = defaultdict(str)

for each in A:
    if each not in freq:
        freq[each] =1
    else:
        freq[each] +=1

print(freq)

max_len = 0
odd_count =1
for each in freq:
    # print(freq[each])
    # while taken_one == False:
    if freq[each] % 2 ==1:
        max_len += freq[each] -1
        odd_count = 1
    else:
        max_len +=freq[each]

max_len +=odd_count


print('final ans:', max_len)
