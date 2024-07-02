'''Problem Description
Alex has a cat named Boomer. He decides to put his cat to the test for eternity.

He starts on day 1 with one stash of food unit, every next day, the stash doubles.

If Boomer is well behaved during a particular day, only then she receives food worth equal to the stash produced on that day.

Boomer receives a net worth of A units of food. What is the number of days she received the stash?'''

A = 10


def checkBit(N, i):
    if N & 1 << i == 0:
        return False
    else:
        return True

def CountGoodDays(N):
    count = 0
    for i in range(32):
        if checkBit(N, i):
            count +=1
    return count

print(CountGoodDays(A))
