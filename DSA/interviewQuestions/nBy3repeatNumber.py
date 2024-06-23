'''Problem Description
You're given a read-only array of N integers. Find out if any integer occurs more than N/3 times in the array in linear time and constant additional space.
If so, return the integer. If not, return -1.

If there are multiple solutions, return any one.

Note: Read-only array means that the input array should not be modified in the process of solving the problem'''

# A = [1,2,3 ,1 ,1]
# A=[ 1, 1, 1, 2, 3, 5, 7 ]

A= [1, 2, 3]
A.sort()
print(A)
element = A[0]
# count = 1
n = len(A)
threshold = n//3
print("threshold: ", threshold)

element_count = dict()
element_count[A[0]] = 1
# print(element_count)
for i in range(1, n):
    if A[i] == A[i-1]:
        element_count[A[i]] = element_count[A[i-1]] + 1
    else:
        element_count[A[i]] = 1

print(element_count)
keys = element_count.keys()
values = element_count.values()
for element, count in element_count.items():
    if count > threshold:
        print("Winner is: ", element)
        break
    else:
        print('No winner found!')