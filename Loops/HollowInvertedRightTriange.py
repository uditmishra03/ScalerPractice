'''Problem Description:

Write a function to print a pattern similar to the one shown in the sample using n which is given to you as an argument to a function. Here n defines the number of rows.

Note: There are no spaces between the stars in the first row, and there are no spaces at the end of each row.

Input Format:

The only argument to the function in an integer n.
Output Format:

Print Star Pattern in string format for each testcase.
Sample Input:

8
Sample Output:

********
*     *
*    *
*   *
*  *
* *
**
*
'''

num = int(input("Enter the size of the star: "))

# num = 10
for i in range(num, 0, -1):

    if i != num and i >= 3:
        print('*'+' '*(i-2)+'*')
    else:
        print('*'*i)