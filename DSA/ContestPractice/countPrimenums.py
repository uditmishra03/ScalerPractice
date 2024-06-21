'''You will be given an integer n. You need to return the count of prime numbers less than or equal to n.'''
import math

n =19
# n =50
ans  = 0


if n ==1:
    ans = 1
else:
    for num in range(2, n+1):
        isPrime = True
        # print('Checking for:', num)
        for j in range(2, int(math.sqrt(num))+1):
            # print(j)
            if num % j == 0:
                isPrime = False

        if isPrime:
            # print('Prime num:', num)
            ans +=1


print('ans:', ans)