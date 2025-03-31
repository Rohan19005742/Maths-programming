import math

def get_factors(num):
    factors = []
    for x in range(2,int(math.sqrt(num))+1):
        if num % x == 0:
            factors.append(x)
            if int(num//x) not in factors:
                factors.append(int(num//x))
    return factors

def is_abundant(num):
    return sum(get_factors(num)) > num

def solve():
    answer=0
    abundant_numbers = []
    dic ={}
    for x in range(28123):
        dic[x+1] = 0
    
    for y in range(1,28123):
        if is_abundant(y):
            abundant_numbers.append(y)
    for u in range(len(abundant_numbers)):
        for v in range(len(abundant_numbers)):
            dic.pop(abundant_numbers[u]+abundant_numbers[v], None)
    
    for key in dic:
        answer+=key
    print(answer)

solve()


