# A = 10
# B = 23
# C = [86, 63, 60, 0, 47, 0, 99, 9, 0, 0]

A = 1
B = 1
C = [2]

ballpossession = []

ballpossession.append(B)

print("First possession is with:", ballpossession[-1])

for i in range(A):
    if C[i] == 0:
        print("backpass", ballpossession.pop())
    else:
        ballpossession.append(C[i])


print("Final stack", ballpossession)

print("final ans: ", ballpossession[-1])

