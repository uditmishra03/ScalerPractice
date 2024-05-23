"""Input Format: N = 3
Result:
  *
 ***
*****
Input Format: N = 6
Result:
     *
    ***
   *****
  *******
 *********
***********
"""

num = 8
rowlength = 1+2*(num-1)
# print(rowlength)
star = '*'
for i in range(1, num+1):
    # print(i)
    for j in range(num-i):
        print(' ', end ='')
    for k in range(2*i-1):
        print(star, end ='')
    print()

# for i in range(0, num):
#     noOfStars = 2*i+1
#     noOfspaces = rowlength - noOfStars
#     print(' '*int(noOfspaces/2)+star*noOfStars+' '*int(noOfspaces/2))
