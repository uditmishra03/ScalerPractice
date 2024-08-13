'''Problem Description
Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.

Refer to the examples for more clarity.'''

# A = "{([])}"

A = '(){'

# A = '()[]'


def BalanceParanthesis(A):
    para_stack = []

    for i in A:
        if i in '([{':
            para_stack.append(i)
        else:
            if len(para_stack) == 0:
                return 0
            else:
                if i == ')':
                    if para_stack[-1] == '(':
                        para_stack.pop()
                    else:
                        return 0
                if i == ']':
                    if para_stack[-1] == '[':
                        para_stack.pop()
                    else:
                        return 0
                if i == '}':
                    if para_stack[-1] == '{':
                        para_stack.pop()
                    else:
                        return 0
    if len(para_stack) > 0:    # Means there are braces left in the stack.
        return 0
    return 1                   # All the paired braces have been popped up.


print(BalanceParanthesis(A))