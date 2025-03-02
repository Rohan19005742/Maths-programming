import math

def number_of_factors(num):
    number_of_factors = 1
    for x in range(1,int(math.sqrt(num))+1):
        if num % x == 0:
            number_of_factors+=2
    return number_of_factors

def solve():
    number = 1
    count = 2
    while True:
        number+=count
        count+=1
        if number_of_factors(number) > 500:
            print(number)
            break

solve()