A = [10, 5, 3, 4, 3, 5, 6]

freq = {}

for i in A:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] +=1

print(freq)

for i in freq:
    if freq[i] > 1:
        print(i, end=' ')

    # print(freq[i])

print()