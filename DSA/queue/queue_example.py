from collections import deque

qu = deque()

print(qu)

qu.append('First')

print(qu)

qu.append("second")

qu.append('Third')

print(qu.pop())

print(qu)

qu.append('Four')
qu.append('Five')
qu.popleft()
print(qu)

if qu :
    print('Yes, exist')
else:
    print("Does not exist")


print(qu)
print(qu[0])
print(qu.popleft())
print(qu)
print(qu[-1])
# while qu:
#     qu.pop()

# print('Check now, length:')


# if qu :
#     print('Yes, exist')
# else:
#     print("Does not exist")
