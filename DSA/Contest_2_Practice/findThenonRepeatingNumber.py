arr = [4,5,5,4,1,6,6]

xor = arr[0]
for i in range(1, len(arr)):
    xor = xor ^ arr[i]

# print(xor)

if xor == 0:
    print('No such element found.')
else:
    print(xor, 'is repeating only once.')
