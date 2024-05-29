# Python for prefix sum
class Solution:
# @param A : list of integers
# @param B : list of list of integers
# @return an list of long
    def rangeSum(self, A, B):
        n, m = len(A), len(B)
        pref = [0 for i in range(n + 1)]
        pref[0] = A[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + A[i]
            ans = [0 for i in range(m)]

        for i in range(m):
            if B[i][0] > 0:
                ans[i] = pref[B[i][1]] - pref[B[i][0] - 1]
            else:
                ans[i] = pref[B[i][1]] - 0


        return ans