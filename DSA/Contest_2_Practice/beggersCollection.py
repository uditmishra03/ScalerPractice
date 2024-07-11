# A = 5
# B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

# Be very cautious about the indexing, double check if it is 0-based or 1-based.

A = 7
B = [[1, 3, 2], [2, 5, 3],[5, 6, -1]]

collection = [0]*A
ans = []
for i in range(len(B)):
    # print(B[i])
    start = B[i][0]
    end = B[i][1]
    value = B[i][2]
    # print(start, end, value)
    collection[start] += value

    if end+1 <A:
        collection[end+1] -= value


    # print(collection)

ans = [0]*A
ans[0] = collection[0]
for i in range(1, A):
    ans[i] = ans[i-1] + collection[i]

print('final ans: ', ans)

