''' Find Palindromes:

Input: Two Number n and m

Output: Count of Palindromes between n and m excluding inputs'''

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# start =100
# end = 117

palindromeCount = 0

# Using the loop and modulo method
def reverse_num(num):
    reverse_num =0
    while num > 0:
        reverse_num = reverse_num*10 + num %10
        num = num // 10
    return  reverse_num

for num in range(start, end+1):
    # Using string slicing.
    rev_num = int(str(num)[::-1])
    # rev_num = reverse_num(num)
    if rev_num == num:
        palindromeCount +=1
        # print(rev_num, num)
print("Palindrome count : ", palindromeCount)
