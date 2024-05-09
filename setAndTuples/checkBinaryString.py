'''Question-2:
Take a string as input.
and check if it's binary string(Contains only 0 and 1)

Sample input 1
"0011010101ab"
Sample output 1
"Not Binary!"

Sample input 2
"010010101010"
Sample output 2
"Binary!"'''

# input_string = input("Enter the string: ")
input_string = "0011010101ab"
# input_string = "010010101010"

input_string_set = set(input_string)

if len(input_string_set) == 2 and '0' in input_string_set and '1' in input_string_set:
    print(f"{input_string} is binary string.")
else:
    print(f"{input_string} is not binary string.")
