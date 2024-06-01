"""Problem Description
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit."""

# A = [1, 2]
# Input 2:
import sys

# A = [1, 4, 5, 2, 4]
min_val = min(A, default=0)
max_val = max(A, default=0)
# print(min_val, max_val)
latest_min, latest_max = -1, -1
# ans = sys.maxsize
profit = 0
for i in range(0, len(A)):
    if i < latest_max and A[i] == min_val:
        latest_min = i
    if A[i] == max_val:
        latest_max = i
    print(latest_min, latest_max)
    if latest_min < latest_max != -1 and latest_min != -1:
        profit = abs(A[latest_min] - A[latest_max])

print(min_val, max_val)
# print(latest_min, latest_max)
print(A[latest_min], A[latest_max])
print(profit)


