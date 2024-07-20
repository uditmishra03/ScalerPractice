'''Problem Description
You are given an array A of N integers. Return the count of elements with frequncy 1 in the given array.'''

# A = [3, 4, 3, 6, 6]
A = [3, 3, 3, 9, 0, 1, 0]

freqArr = {}

for i in A:
    if i not in freqArr:
        freqArr[i] =1
    else:
        freqArr[i] +=1

print(freqArr)
uniqueCount =0
for each in freqArr.values():
     if each == 1:
        uniqueCount +=1

print('final ans: ', uniqueCount)