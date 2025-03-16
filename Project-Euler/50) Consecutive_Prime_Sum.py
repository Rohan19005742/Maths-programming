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



def solve():
    primes = []
    for x in range(1,10000):
        if is_prime(x):
            primes.append(x)
    left = 0
    right = 1

    answer = 0
    longest = 0
    while left != len(primes) - 1:
        summation = sum(primes[left:right])
        if summation >= 1000000:
            left+=1
            right = left+1
        else:
            if is_prime(summation):
                count = right - left
                if count > longest:
                    longest = count
                    answer = summation
            if right != len(primes) -1:
                right+=1
            else:
                left+=1
    
    print(answer)




    

solve()