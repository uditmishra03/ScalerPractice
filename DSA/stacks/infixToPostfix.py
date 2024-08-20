def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def associativity(c):
    if c == '^':
        return 'R'
    return 'L'  # Default to left-associative

def infix_to_postfix(s):
    result = []
    stack = []

    for i in range(len(s)):
        c = s[i]

        # If the scanned character is an operand, add it to the output string.
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
            result.append(c)
        # If the scanned character is an ‘(‘, push it to the stack.
        elif c == '(':
            stack.append(c)
        # If the scanned character is an ‘)’, pop and add to the output string from the stack
        # until an ‘(‘ is encountered.
        elif c == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # Pop '('
        # If an operator is scanned
        else:
            while stack and (prec(s[i]) < prec(stack[-1]) or (prec(s[i]) == prec(stack[-1]) and associativity(s[i]) == 'L')):
                result.append(stack.pop())
            stack.append(c)

    # Pop all the remaining elements from the stack
    while stack:
        result.append(stack.pop())

    print(''.join(result))

# Driver code
# exp = "a+b*(c^d-e)^(f+g*h)-i"
# A = "x^y/(a*z)+b"
# A = "a+b*(c^d-e)^(f+g*h)-i"
A = 'c*(u-p)^e/(w*x^p)^k^(d^o)'

# Function call
infix_to_postfix(A)
