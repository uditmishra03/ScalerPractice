'''Print N numbers in Decreasing Order and then in Increasing Order.

You are given a positive number N.
You are required to print the numbers from N to 1.
You are required to not use any loops. Don't change the signature of the function DecThenInc function.'''



def decthenInc(num):
    if num == 0:
        # print(num, num, sep =' ', end =' ')
        return
    print(num, end =' ')
    decthenInc(num-1)
    print(num, end =' ')
    

decthenInc(5)
print()