'''Question-1:
Take a string as input.
Print the number of unique characters in that string.'''

# input_string = input("Enter the string: ")

# input_string = "Mississippi"
input_string = "The jovial crew zigzagged quickly through the fog, hoping to vanquish the mythical kraken."
# Approach one converting string to set.
print("*** Approach #1 ***")
input_string_set = set(input_string)
print(f"Total number of unique characters: {len(input_string_set)} which are \n {input_string_set}")

# Approach two adding each char to set.
print("\n*** Approach #2 ***")
out_set = set()
for each in input_string:
    out_set.add(each)
print(f"\nset: {out_set} and Length : {len(out_set)}")
