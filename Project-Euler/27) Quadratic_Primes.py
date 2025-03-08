import math

def is_prime(num):
    if num <= 0:
        return False
    if num == 1 or num == 2:
        return True
    for x in range(2,int(math.sqrt(num))+1):
        if num % x == 0:
            return False
    return True


def prime_counts(a,b):
    count = 0
    while True:
        if is_prime(count*count + a*count + b):
            count+=1
        else:
            break
    return count

def solve():
    maxi = 0
    a_val = 0
    b_val = 0
    for a in range(1,1000):
        for b in range(1,1000):
            count = prime_counts(a,b)
            if count > maxi:
                maxi = count
                a_val = a
                b_val = b
    for a1 in range(-1000,0):
        for b1 in range(1,1000):
            count = prime_counts(a1,b1)
            if count > maxi:
                maxi = count
                a_val = a1
                b_val = b1
    for a2 in range(1,1000):
        for b2 in range(-1000,0):
            count = prime_counts(a2,b2)
            if count > maxi:
                maxi = count
                a_val = a2
                b_val = b2
    

    print(a_val * b_val)
    print(maxi)

solve()