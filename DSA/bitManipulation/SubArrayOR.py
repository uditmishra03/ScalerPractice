'''Problem Description
You are given an array of integers A of size N.

The value of a subarray is defined as BITWISE OR of all elements in it.

Return the sum of value of all subarrays of A % 109 + 7.'''

# Explanation:
# Iterate through bits: Loop from 0 to 31 (for 32-bit integers) to consider each bit position.
# Calculate contribution of current bit:
# For each bit position i, calculate the number of subarrays that do not have the ith bit set.
# This is done using a suffix_sum array and a cnt variable.
# cnt keeps track of the number of consecutive elements with the ith bit unset.
# suffix_sum stores the cumulative sum of cnt values from the right.
# Calculate total contribution:
# The total number of subarrays is n * (n + 1) / 2.
# Subtract the number of subarrays that do not have the ith bit set from the total number of subarrays.
# This gives us the number of subarrays that do have the ith bit set.
# Multiply this number by 2**i (the value of the bit at position i) and add it to the total_sum.
# Return total sum: After processing all bit positions, return the total_sum.
# Time complexity: O(n * log(max(arr)))

# A = [1, 2, 3, 4, 5]
# A = [1, 2, 3, 4]
A = [7, 8, 9, 10]



def checkBit(N, i):
    if N & (1 << i) == 0:
        return False
    else:
        return True
    

def sumOfN(n):
    return int((n*(n+1))/2)

n = len(A)
noOfSubarray = sumOfN(n)

print('no of subarray: ', noOfSubarray)

total = 0
max_bits= len(bin(max(A))[2:])

print("max bits required: ", max_bits)

for i in range(max_bits):
    suffix_sum = 0
    zero_count = 0
    for j in A[::-1]:
        # print('chjecking for value: ', j)
        if checkBit(j, i) == False:
            # print(i, 'th bit is not set for ', j)
            zero_count +=1
        else:
            zero_count = 0
        suffix_sum += zero_count
    
    print(suffix_sum, noOfSubarray, total)
    total += (1<<i)*(noOfSubarray- suffix_sum)


print(total%(10**9+7))

