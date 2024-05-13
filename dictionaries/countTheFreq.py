input_string = "mississipi"

dict1 = {}
for i in input_string:
    dict1.update({i: input_string.count(i)})

print(dict1)