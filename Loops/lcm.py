A = 6
B = 4

maxofTwo = max(A, B)
# print(maxofTwo)
while maxofTwo > 0:
    if maxofTwo % A == 0 and maxofTwo % B == 0:
        # print(maxofTwo)
        break
    maxofTwo += 1

print(maxofTwo)