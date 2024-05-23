"""Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the Reverse N-Star Triangle.

Example:
Input: ‘N’ = 3

Output:

*****
 ***
  *"""
num = 5
for i in range(num, 0 , -1):
    # print(i)
    for k in range(num - i):
        print(' ', end ='')
    for j in range(2*i-1):
        print('*', end ='')
    print()