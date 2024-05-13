'''Print list in reverse order using a loop
Given:

list1 = [10, 20, 30, 40, 50]'''

list1 = [10, 20, 30, 40, 50]

for i in list1[::-1]:
    print(i, end =' ')

print("\n", 10*'*', sep ='')
rev_list1 = reversed(list1)
for each in rev_list1:
    print(each, end =' ')