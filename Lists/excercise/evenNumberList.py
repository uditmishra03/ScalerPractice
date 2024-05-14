'''Exercise 8: Generate a Python list of all the even numbers between 4 to 30'''

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# start = 4
# end = 30

# while start < end:
#     if start % 2 == 0:
#         print(start, end =', ')
#     start +=1

if start % 2 !=0:
    start +=1
for each in range(start, end, 2):
    print(each, end =', ')