import math

def digit_factorial(num):
    num = str(num)
    total = 0
    for n in num:
        total+=math.factorial(int(n))
    return total

def solve():
    total = 0
    for x in range(10,1000000):
        if digit_factorial(x) == x:
            total+=x
    print(total)

solve()