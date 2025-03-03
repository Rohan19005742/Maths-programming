def sum_of_digits(num):
    num = str(num)
    total = 0
    for n in num:
        total += int(n)
    return total

def factorial(num):
    total = 1
    for x in range(num,1,-1):
        total*=x
    return total

print(sum_of_digits(factorial(100)))