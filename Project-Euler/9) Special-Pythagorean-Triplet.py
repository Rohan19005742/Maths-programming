import math

def is_pbthagorean_triplet(num1,num2):
    c = num1 * num1 + num2 * num2
    root = math.sqrt(c)
    return int(root) * int(root) == c

def special():
    for a in range(1,3000):
        for b in range(1,3000):
            if is_pbthagorean_triplet(a,b):
                c = math.sqrt(a*a + b*b)
                if a+b+c == 1000:
                    return int(a*b*c)
                
print(special())