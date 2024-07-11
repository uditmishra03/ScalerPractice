A = [5, -2, 3 , 1, 2]
B = 3

print(A)
n = len(A)
# print(A, '\n')

pfsum = [0] * len(A)
pfsum[0] = A[0]
for i in range(1, len(A)):
    pfsum[i] = pfsum[i - 1] + A[i]

sfsum = [0] * n
sfsum[n - 1] = A[-1]
for i in range(len(A) - 2, -1, -1):
    sfsum[i] = sfsum[i + 1] + A[i]

print ('\npfsum:', pfsum, '\nsfsum: ', sfsum, sep = '\n')


ans = max(pfsum[B - 1], sfsum[n - B])   # 2, 2
# print(ans)
sum = 0
for i in range(1, B):
    # print(f"i: {i}")
    sum = pfsum[i - 1] + sfsum[n -(B -i)]
    ans = max(ans, sum)

print(ans)