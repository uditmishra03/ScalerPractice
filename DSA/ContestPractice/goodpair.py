A = [1,2,3,4]
B = 7
#
# for i in range(len(A)):
#     for j in range(i + 1, len(A)):
#         print(A[i], A[j])

count =0

for i in range(len(A)):
    for j in range(i, len(A)):
        count +=1
        print(A[i:j+1])

print('Count:', count)