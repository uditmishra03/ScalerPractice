'''Exercise 15: Use a loop to display elements from a given list present at odd index positions

AD
Given:

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]'''

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in range(1, len(my_list), 2):
    print(my_list[i], end = ' ')
