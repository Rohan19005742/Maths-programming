def solve():
    answer = set()
    for a in range(2,101):
        for b in range(2,101):
            answer.add(pow(a,b))
    print(len(answer))

solve()