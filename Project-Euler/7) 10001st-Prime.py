import math

def is_prime(num):
    if num == 1 or num == 2:
        return True
    for x in range(2,int(math.sqrt(num))+1):
        if num % x == 0:
            return False
    return True

def find_prime(index):
    primes = 0
    count = 2
    while primes != index:
        if is_prime(count):
            primes+=1
        count+=1
    return count-1

print(find_prime(10001))
