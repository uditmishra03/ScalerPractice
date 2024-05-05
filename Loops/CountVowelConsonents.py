''' Vowel/Consonant Count:

Input: A string

Output: Print the number of vowels and consonants in the string'''

inputString = 'hello world'
# inputString= 'Print the number of vowels and consonants in the string'
# print(len(inputString))
vowelCount = 0
consonantsCount = 0
for ch in inputString:
    if ch in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        vowelCount +=1
    else:
        consonantsCount +=1

print(f"Vowels: {vowelCount}, Consonants: {consonantsCount}")