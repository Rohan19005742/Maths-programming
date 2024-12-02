'''
Description of problem: Start with any positive integer n. If n is even divide by 2 else multiply by 3 and add 1, carry this on until it reaches 1.
It is yet to be proven that there is a number n that does not endup at 1.
'''


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