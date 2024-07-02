'''Problem Description
Write a function that takes an integer and returns the number of 1 bits present in its binary representation.'''



A = 15
def countBits(num):
    count = 0
    bin_of_num = bin(num)[2:]
    # print(bin_of_num)

    for bit in bin_of_num:
        if bit == '1':
            count +=1

    # print(count)
    return count

print(countBits(A))