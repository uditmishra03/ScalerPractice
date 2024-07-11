'''You are given a string S, and you have to find all the amazing substrings of S.

An amazing Substring is one that starts with a vowel (a, e, i, o, u, A, E, I, O, U).'''

vowels = ('a', 'e', 'i', 'o', 'u', 'E', 'A', 'I', 'O', 'U')
# print(vowels)

A = 'ABEC'
# A ='AZELEA'
# substrings =[]
count = 0
for i in range(len(A)):
    for j in range(i, len(A)):
        # print(A[i:j+1])
        if A[i:j+1].startswith(vowels):
            # print(A[i:j + 1])
            count +=1

print(count%10003)


