import math

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    for x in range(2,int(math.sqrt(num))+1):
        if num % x == 0:
            return False
    return True

def prime_factors(num):
    factors = []
    x = 1
    while num > 1:
        x+=1
        while num % x == 0 and is_prime(x):
            num = num // x
            count = x
            while num % x == 0:
                num = num // x
                count *=x
            if count not in factors:
                factors.append(count)
    return factors

def solve():
    prev = []
    factors = []
    for x in range(10,10000000):
        prime_fac = prime_factors(x)
        if len(prime_fac) != 4:
            prev = []
            factors = []
            continue
        prev.append(x)
        for num in prime_fac:
            if num in factors:
                prev = []
                factors = []
                break
            else:
                factors.append(num)
        if len(prev) == 4:
            break
    print(prev)
solve()