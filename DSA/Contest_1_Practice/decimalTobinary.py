num = 10

bin = ''

while num > 0:
    remainder = num % 2
    bin = str(remainder) + bin
    # print('bin: ', bin)
    num = num //2
    # print(f"num: ", num)

print(bin)