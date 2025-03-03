def sum_of_digits(num):
    num = str(num)
    total = 0
    for n in num:
        total += int(n)
    return total

print(sum_of_digits(2**1000))