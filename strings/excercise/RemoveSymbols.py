"""Exercise 15: Remove special symbols / punctuation from a string
Given:

str1 = "/*Jon is @developer & musician"""


str1 = "/*Jon is @developer & musician"
# str1_list = str1.split()
# print(str1_list)

clean_str = ''
for each in str1:
    if each.isalpha() or each.isspace():
        clean_str += each

print(clean_str)
