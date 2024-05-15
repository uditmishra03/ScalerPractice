'''Exercise 14: Remove empty strings from a list of strings
Given:

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]'''

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

str1 = []

for each in str_list:
    if each:
        # print("true")
        str1.append(each)

print(str1)

new_list = list(filter(None, str_list))

print(new_list)