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
    answer = 0
    count = 0
    for x in range(10,1000000):
        if is_prime(x):
            trunable = True
            num = str(x)
            for n in range(len(num)-1):
                num = num[1:]
                if not is_prime(int(num)):
                    trunable = False
                    break
            num1 = str(x)
            for n in range(len(num1)-1):
                num1 = num1[:len(num1)-1]
                if not is_prime(int(num1)):
                    trunable = False
                    break

            if trunable:
                count+=1
                answer+=x

    print(answer)
    print(count)
solve()

