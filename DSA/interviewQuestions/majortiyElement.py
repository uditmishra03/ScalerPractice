'''Problem Description
Given an array of size N, find the majority element. The majority element is the element that appears more than floor(n/2) times.
You may assume that the array is non-empty and the majority element always exists in the array.

'''

# Input 1:
A= [2, 1, 1]
# Input 2:
# A=[1, 1, 1]

element = A[0]
count = 1
n = len(A)

for i in range(1, n):
    if A[i] == element:
        count +=1
    else:
        if count > 0:
            count -=1
        else:
            element = A[i]
            count = 1
# print(element, count)

# print(element)
# check if element is majority element.
count_of_element =0
for i in range(n):
    if A[i] == element:
        count_of_element +=1

print(element, count_of_element, n//2)
if(count_of_element > n//2):
    print("majority element:  ", element)
else:
    print('No majority element.')