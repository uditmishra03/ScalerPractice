'''Exercise 5: Count all letters, digits, and special symbols from a given string
Given:'''


def findCounts(string):
    alpha_count, num_count, symbol_count = 0, 0, 0
    for char in str1:
        if char.isalpha():
            alpha_count += 1
        elif char.isnumeric():
            num_count += 1
        else:
            symbol_count += 1

    print(
        f'''Total counts of chars, digits, and symbols\nChars = {alpha_count}\nDigits = {num_count}\nSymbol = {symbol_count}''')


str1 = "P@#yn26at^&i5veakjhgakfgh"

findCounts(str1)
