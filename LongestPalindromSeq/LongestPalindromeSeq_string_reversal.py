'''Finding the length of Longest Palindromic Subsequence
Given a string, the longest palindromic subsequence (LPS) is the maximum-length subsequence that reads the same backward as forward. A subsequence is a sequence that can be derived from the original sequence by deleting some or no elements without changing the relative order of the remaining elements.

Task: Write a function or algorithm that efficiently finds the length of the LPS in a given string.

Sample Inputs and Outputs:

Input String	Longest Palindromic Subsequence (Length)
"LEEKEESEE"	5 (EEKEE or EESEE or others)
"BBABCBAB"	7 (BABCBAB)
"cbbd"	2 (bb)
"a"	1 (a)
Explanation:

In "LEEKEESEE", the longest palindromic subsequences are "EEKEE", "EESEE", both with a length of 5.
In "BBABCBAB", the entire string itself is a palindrome, resulting in a longest subsequence length of 7.
In "cbbd", "bb" is the longest palindrome of length 2.
In "a", the single character "a" is a palindrome of length 1.
Constraints:

The input string can have a length between 1 and 1000 characters (inclusive).
The string consists only of lowercase English letters.
Bonus:

Can you modify your solution to also return an actual longest palindromic subsequence string, not just its length?
Variations of Above Question:
1) Find Total Number of Palindrome subsequences

2) Return the largest Size Palindrome, if multiple palidromes are of Equal Max Size return all.

3) Return All subsequence Palindromes as List'''

# test_string= "BBABCBAB"
# test_string = 'cbbd'
# test_string = 'a'
# test_string = "abcd"


test_string = "LEEKEESEE"

# 1. Create sub-string from the original string
# 2. check for palindrome for the substring.

# lambda function for the reversal of string.
test_string = test_string.lower()

reversal_string = lambda word: word[::-1]
# sorted_list = lambda str_list:
# sorted_list = sorted(str_list, key=lambda x: len(x))

def getLSP(phrase):
    max_len_LPS = 0
    total_palindrome_count = 0
    lps = ''
    all_palindromes = []
    palindromes = []
    max_len_subsequences = []
    # print("length of string: ", len(test_string))

    for i in range(1, len(phrase) + 1):
        for j in range(i):
            subsequence = phrase[j:i:]
            rev_subsequence = reversal_string(subsequence)
            # Getting all the palindromes.
            if subsequence == rev_subsequence:
                all_palindromes.append(subsequence)
            # Getting only unique palindromes
            if subsequence == rev_subsequence and subsequence not in palindromes:
                total_palindrome_count += 1
                palindromes.append(subsequence)
            # getting only max len palindromes with sequence.
            if subsequence == rev_subsequence and max_len_LPS <= len(subsequence):
                max_len_LPS = len(subsequence)
                lps = subsequence

    for seq in all_palindromes:
        if len(seq) == max_len_LPS:
            max_len_subsequences.append(seq)
    palindromes.sort(key=lambda x: len(x))

    print(f"maximum length of LPS: {max_len_LPS}, and the LPS is: \"{lps}\"")
    print(f"\nAll the subsequnces of maximum length of LPS: {max_len_LPS} are : {max_len_subsequences}")
    print("\nTotal unique palindromic sequence:", total_palindrome_count)
    print("\nAll the unique palindromes found")
    for i in range(len(palindromes)):
        print(f"{i + 1}. {palindromes[i]}: {len(palindromes[i])}")

getLSP(test_string)


# print(f"maximum length of LPS: {max_len_LPS}, and the LPS is: \"{lps}\"")
# print(f"All the subsequnces of maximum length of LPS: {max_len_LPS} are : {max_len_subsequences}")
# print("\nTotal unique palindromic sequence:", total_palindrome_count)
# print("\nAll the unique palindromes found")
# # for i in range(len(palindromes)):
#     print(f"{i + 1}. {palindromes[i]}: {len(palindromes[i])}")
