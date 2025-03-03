import math

def factors(num):
    factors = []
    for x in range(1,int(math.sqrt(num))+1):
        if num % x == 0:
            factors.append(x)
            factors.append(int(num/x))
    factors.remove(num)
    return factors

def sum_amicable_numbers(upTo):
    answer = 0

    for x in range(1,upTo+1):
        fact = factors(x)
        d_x = sum(fact)
        fact2 = factors(d_x)
        d_d_x = sum(fact2)
        if d_d_x == x and d_x != x:
            print(x)
            print(d_x)
            answer+=d_x + x
    return int(answer / 2)

print(sum_amicable_numbers(10000))
