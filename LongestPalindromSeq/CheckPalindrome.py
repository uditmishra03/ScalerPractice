test_string = "udit"

isPalindrome = True
for i, j in zip(range(len(test_string)), range(len(test_string)-1, -1, -1)):
    # print(i, j)
    # print(i, test_string[i] , j, test_string[j])
    if test_string[i] != test_string[j]:
        isPalindrome = False
        break

if isPalindrome == True:
    print(f"{test_string} is a palindrome.")
else:
    print(f"{test_string} is not a palindrome.")


