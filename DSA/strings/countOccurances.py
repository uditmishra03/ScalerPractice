'''Problem Description
Find the number of occurrences of bob in string A consisting of lowercase English alphabets.'''

# Input 1:
# word= "abobc"
# Input 2:
word = "bobob"

count =0
phrase = 'bob'
phrase_len= len(phrase)
if phrase_len > len(word):
    count = 0

start = 0
end = phrase_len
while phrase_len <= len(word):
    substring = word[start:phrase_len]
    # print(substring)
    if substring == phrase:
        count +=1
    start +=1
    phrase_len +=1

print(count)