def pentagon_number(n):
    return n * (3 * n - 1) // 2

def is_pentagon_number(n):
    n *= 2
    a = 3
    b = -1
    c = -n
    d = b ** 2 - 4 * a * c
    if d < 0:
        return False
    x = (-b + d ** 0.5) / (2 * a)
    if x.is_integer():
        return True
    return False

def solve():
    for j in range(1, 10000):
        for k in range(j + 1, 10000):
            if is_pentagon_number(pentagon_number(k) - pentagon_number(j)) and is_pentagon_number(pentagon_number(k) + pentagon_number(j)):
                print(pentagon_number(k) - pentagon_number(j))
                return
solve()