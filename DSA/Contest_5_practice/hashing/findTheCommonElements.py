from collections import defaultdict

# A = [1, 2, 2, 1]
# B = [2, 3, 1, 2]

A = [2, 1, 4, 10]
B = [3, 6, 2, 10, 10]

freq_A, freq_B = defaultdict(int), defaultdict(int)


def count_freq(arr):
    freq = defaultdict(int)
    for i in arr:
        freq[i] +=1

    return freq

freq_A = count_freq(A)
freq_B = count_freq(B)

print(freq_B, freq_A)

ans = []
for each in freq_B:
    if each in freq_A:
        for j in range(min(freq_B[each], freq_A[each])):
            ans.append(each)
ans.sort()
print('Final ans:', ans )
