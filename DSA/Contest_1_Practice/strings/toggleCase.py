A = "RamSharaN"

A_toggled = ''
for char in A:
    if char >='a' and char <='z':
        A_toggled += chr(ord(char)-32)
    else:
        # print('caps:', char)
        A_toggled += chr(ord(char) + 32)

print(A_toggled)