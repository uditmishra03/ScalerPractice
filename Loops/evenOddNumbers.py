num = int(input("Enter the number: "))

for i in range(1, num+1):
    if i % 2 ==0:
        if i == num:
            print(i, end='')
        else:
            print(i, end=', ')