from itertools import permutations

def solve():
    digits = '0123456789'
    perms = permutations(digits)
    perms = sorted([''.join(p) for p in permutations(digits)])
    answer = int(perms[999999])
    print(answer)

solve()