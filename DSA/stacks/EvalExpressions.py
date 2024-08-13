# A =   ["2", "1", "+", "3", "*"]

A = ["4", "13", "5", "/", "+"]

def calcPostfix(A):
    calc_stack = []
    second , first = 0, 0
    for i in A:
        if i in '+*-/':
            print("Its an operator", i)
            if len(calc_stack) < 2:
                return 0
            second = calc_stack.pop()
            first = calc_stack.pop()
            if i == '+':
                calc_stack.append(first + second)
            elif i == '-':
                calc_stack.append(first - second)
            elif i == '*':
                calc_stack.append(first * second)
            elif i == '/':
                calc_stack.append(first // second)

        else:
            calc_stack.append(int(i))
   
    if len(calc_stack) == 1:
        return calc_stack[-1]
    else:
        return 0
   



print('Final ans:', calcPostfix(A))