'''Exercise 14: Reverse a given integer number
Given:

76542'''

num = 765425926978
print(int(str(num)[::-1]))

rev_num = 0
while num > 0:
    rev_num = rev_num*10 + num % 10
    # print("rev_num:", rev_num)
    num = num //10
    # print(num)
print(rev_num)