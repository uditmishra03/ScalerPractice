'''Exercise 3: Create a new string made of the first, middle, and last characters of each input string'''
import math


def getPositions(string):
    first = 0
    last = len(string) - 1
    mid = int(math.floor(len(string) / 2))
    return first, mid, last


s1 = "America"
s2 = "Japan"

s1_positions = getPositions(s1)
s2_positions = getPositions(s2)

# print(s1_positions, s2_positions)

for i, j in zip(s1_positions, s2_positions):
    print(s1[i] + s2[j], end='')
