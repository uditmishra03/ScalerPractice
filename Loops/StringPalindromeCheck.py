inputString = "racecar"
reversedString=''
for char in inputString[ : :-1]:
    reversedString+=char
    # print(char, end =' ')
# print(reversedString)

if inputString == reversedString:
    print("Yes")
else:
    print("No")