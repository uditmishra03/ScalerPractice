# A = "((a+b))"
# A = "(a+(a+b))"
A = 'a+b'


def redundantBraces(A):
    arg_stack = []
    
    for i in A:
        count = 0
        if i == ')':
            while arg_stack[-1] != '(':
                arg_stack.pop()
                count +=1
            if count <= 1:
                return 1
            arg_stack.pop()
        else:
            arg_stack.append(i)

    return 0


print('Final ans:', redundantBraces(A))












































        # if i in '(+-*/':
        #     arg_stack.append(i)
        #     print(arg_stack)
        # else:
        #     if len(arg_stack) == 0:
        #         return 1
        #     elif arg_stack[-1] == '(':
        #         return 1
        #     else:
        #         while arg_stack[-1] != '(':
        #             print('Popping:', arg_stack.pop())