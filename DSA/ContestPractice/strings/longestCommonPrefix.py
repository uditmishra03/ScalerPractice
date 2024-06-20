'''Problem Description
Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in the array.

The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1 and S2.

Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".'''

# A = ["abcdefgh", "aefghijk", "abcefgh"]
A = ["abeeab", "abere", "abacd"]

def findprefix(string1, string2):
    ans = ''
    min_len = min(len(string1), len(string2))
    for i in range(min_len):
        if string1[i] == string2[i]:
            # print(string1[i])
            ans += string1[i]
    return ans

print(findprefix())


prefix = []
prefix.append(A[0])

print(prefix[0])
for i in range(1, len(A)):
    print(i, print(A[i]))
#     prefix[i].append(findprefix(prefix[i-1], A[i]))

# print(prefix)
# print(A[0], A[1])
# print(findprefix(A[0], A[1]))
# # ans = findprefix(A[0], A[1])
# print(ans)
