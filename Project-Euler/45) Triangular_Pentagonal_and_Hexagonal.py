import math

def is_triangular(num):
    a = 1
    b = 1
    c = -num*2
    x = int((-b + math.sqrt(b*b - 4*a*c)) / (2*a))
    
    return (x*(x+1) / 2) == num

def is_pentagonal(num):
    a = 3
    b = -1
    c = -num*2
    x = int((-b + math.sqrt(b*b - 4*a*c)) / (2*a))
    
    return (x*(3*x-1) / 2) == num

def is_hexagonal(num):
    a = 2
    b = -1
    c = -num
    x = int((-b + math.sqrt(b*b - 4*a*c)) / (2*a))
    
    return x*(2*x-1) == num

def get_triangle(n):
    return int(n*(n+1)/2)

def get_pentagonal(n):
    return n*(3*n-1)/2

def get_hexagonal(n):
    return n*(2*n-1)

def solve():
    triangle = {}
    pentagonal = {}
    hexagonal ={}

    for x in range(2,100000):
        t = get_triangle(x)
        p = get_pentagonal(x)
        h = get_hexagonal(x)
        triangle[t] = t
        pentagonal[p] = p
        hexagonal[h] = h
        if t in pentagonal and t in hexagonal:
            print(t)

solve()