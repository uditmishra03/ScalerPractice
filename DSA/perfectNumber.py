def solve(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        # print('is a perfect number')
        return 1
    else:
        # print('is not a perfect number')
        return 0


result = solve(5)
print(result)