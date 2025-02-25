import math

def is_divisile(num,Range):
    for x in range(2,Range):
        if num % x != 0:
            return False
    return True

def smallest_multiple(Range):
    answer = 1
    squares = []
    for x in range(2,Range+1):
        squares.append(x*x)
        answer *= x
    for num in squares:
        if answer % num == 0:
            answer /= int(math.sqrt(num))
    return int(answer)

print(smallest_multiple(20))

