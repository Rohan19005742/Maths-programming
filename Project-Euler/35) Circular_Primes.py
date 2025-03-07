import math

def is_prime(num):
    if num == 1 or num == 2:
        return True
    for x in range(2,int(math.sqrt(num))+1):
        if num % x == 0:
            return False
    return True

def solve():
    count = 0
    for x in range(2,1000001):
        if is_prime(x):
            rotate = len(str(x)) - 1
            if rotate == 0:
                count+=1
                continue
            num = x
            prime = True
            for y in range(rotate):
                num = str(num)[1:] + str(num)[0]
                if not is_prime(int(num)):
                    prime = False
            if prime:
                count+=1
    print(count)

solve()