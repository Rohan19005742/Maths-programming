import math
from itertools import permutations

def checkPandigital(num):
    num = str(num)
    length = len(num)
    numbers = ["1","2","3","4","5","6","7","8","9"]
    for x in range(length):
        if numbers[x] not in num:
            return False
    return True


def is_prime(num):
    if num == 1 or num == 2:
        return True
    for x in range(2,int(math.sqrt(num))+1):
        if num % x == 0:
            return False
    return True

def solve():
    largest = 0
    for y in range(9,1,-1):
        perm = permutations(["9", "8", "7", "6","5","4", "3", "2", "1"],y) 
        for x in list(perm):
            num = "".join(x)
            if checkPandigital(num) and is_prime(int(num)):
                largest = max(largest, int(num))
    print(largest)

solve()