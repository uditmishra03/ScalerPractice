num = int(input("Enter the number: "))

sum =0
for i in range(1, num+1):
    sum +=i
print("forsum: ", sum)

whileSum = 0
while num >0:
    whileSum +=num
    num -=1
print("While sum: ", whileSum)