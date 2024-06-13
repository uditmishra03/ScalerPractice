num = 10

bin = ''

while num > 0:
    bin = str(num % 2) + bin
    num = num // 2

print(bin)