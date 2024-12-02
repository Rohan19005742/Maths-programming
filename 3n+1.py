#n = int(input("Enter a number: "))
n = 10e307
print(n)
while n != 1:
    if n % 2 == 1:
        n *= 3
        n += 1
    else:
        n = int(n/2)

print("Ends up at one")