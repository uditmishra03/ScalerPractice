'''Count the total number of digits in a number'''

'''For example, the number is 75869, so the output should be 5.'''

num = 758691415151900834
original_num = num

count = 0

while num >0:
    rem = num % 10
    num //=10
    count +=1

print(f"No of digits in {original_num} are {count}")
print(f"length is {len(str(original_num))}")