def checkPandigital(num):
    num = str(num)
    if len(num) != 9:
        return False
    numbers = ["1","2","3","4","5","6","7","8","9"]
    for n in numbers:
        if n not in num:
            return False
    return True


def solve():
    largest = 0
    for x in range(1,10000000):
        num = str(x)
        count = 1
        while len(num) < 9:
            count+=1
            num+=str(x*count)
        if checkPandigital(num):
            largest = max(largest, int(num))
            print(x)
    print(largest)

solve()

