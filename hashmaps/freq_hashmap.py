class Solution:
# @param A : list of integers
# @param B : list of integers
# @return a list of integers
def solve(self, A, B):
	freq = {}
	ans = []
	for x in A:
		if x not in freq:
			freq[x] = 1
	else:
		freq[x] += 1
	for y in B:
		if y in freq:
		ans.append(freq[y])
	else:
		ans.append(0)
	return ans
