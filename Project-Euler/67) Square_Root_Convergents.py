from fractions import Fraction

def root2():
    num = 1
    dem = 1
    count = 0
    for _ in range(1000):
        num, dem = 2 * dem + num, dem + num
        if len(str(num)) > len(str(dem)):
            count += 1
    return count


print(root2()) 