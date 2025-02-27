import math

def is_prime(num):
    if num == 1 or num == 2:
        return True
    for x in range(2,int(math.sqrt(num))+1):
        if num % x == 0:
            return False
    return True

def summation(limit):
    answer = 0
    for x in range(2,limit):
        if is_prime(x):
            answer+=x
    return answer

print(summation(2000000))