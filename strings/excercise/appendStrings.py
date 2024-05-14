'''Exercise 2: Append new string in the middle of a given string'''

s1 = "Ault"
s2 = "Kelly"

mid = int(len(s1)/2)
# print(mid, s1[:mid:])

new_str = s1[:mid]+s2+s1[mid:]
print(new_str)