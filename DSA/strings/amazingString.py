'''You are given a string S, and you have to find all the amazing substrings of S.
An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).'''

string = 'ABEC'

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
str_len = len(string)
amazing_str_count = 0


for i in range(str_len):
    if string[i] in vowels:
        amazing_str_count += (str_len -i)

print(amazing_str_count % 10003)