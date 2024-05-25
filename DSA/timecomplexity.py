# n =1000
# i = 1
# count = 0
# while i< n:
#     x =i
#     while x > 0:
#         x -=1
#         count +=1
#         print(count)
#     i +=1

s = 0
count = 0
n =100
for i in range(1, n):
    while i**3 <=n:
        s +=1
    count +=1
    print(count)