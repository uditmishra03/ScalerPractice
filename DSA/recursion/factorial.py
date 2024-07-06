def factorial(num):
    if num == 1:
        return 1
    ans = factorial(num-1) * num
    return ans


print(factorial(6))