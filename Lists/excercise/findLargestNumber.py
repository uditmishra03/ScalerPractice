'''Exercise 9: Find the largest item from a given list'''

input_list = [4, 6, 8, 24, 12, 2, 56, 23, 34, 12, 14]

maximum = input_list[0]
for i in range(1, len(input_list)):
    # print(input_list[i])
    if maximum < input_list[i]:
        maximum = input_list[i]

print(f"Largest number in the list is: {maximum}", )


print(f"Direct function: Largest number in the list is: {max(input_list)}" )
