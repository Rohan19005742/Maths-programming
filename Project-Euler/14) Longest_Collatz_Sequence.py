def collatz_squence(num):
    count = 1
    while num != 1:
        count+=1
        if num % 2 == 1:
            num *= 3
            num += 1
        else:
            num = int(num/2)
    return count

def solve():
    maxi = 0
    num = 0
    for x in range(1,1000000):
        count = collatz_squence(x)
        if  count > maxi:
            maxi = count
            num = x
    print(num)

solve()