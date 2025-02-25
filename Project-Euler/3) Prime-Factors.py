import math

def is_prime(num):
    if num == 1 or num == 2:
        return True
    for x in range(2,int(math.sqrt(num))+1):
        if num % x == 0:
            return False
    return True

def largest_prime_factor(num):
    factors = []
    for x in range(2,int(math.sqrt(num))+1):
        if num % x == 0:
            factors.append(x)
    
    for y in range(len(factors)-1,-1,-1):
        if is_prime(factors[y]):
            return factors[y]

print(largest_prime_factor(600851475143))
        

