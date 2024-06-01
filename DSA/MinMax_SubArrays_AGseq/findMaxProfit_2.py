# A = [1, 4, 5, 2, 4]
# A= [3, 5, 7, 2,4, 3, 8, 6]
A = [2, 1]
n = len(A)
maxProfit = 0
max_val = A[-1]

# print(maxProfit, max_val)

for i in range(n-2, -1, -1):
    if A[i] > max_val:
        max_val = A[i]
    profit = max_val - A[i]
    if maxProfit < profit:
        maxProfit = profit

print(maxProfit)

