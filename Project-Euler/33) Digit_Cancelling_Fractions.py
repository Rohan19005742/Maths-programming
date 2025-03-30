def solve():
    answer = 1

    for i in range(10, 100):
        for j in range(10, 100):
            if i == j:
                continue
            if i % 10 == 0 and j % 10 == 0:
                continue
            first = i // 10
            second = i % 10
            third = j // 10
            fourth = j % 10

            if second == third:
                if fourth != 0 and i / j == first / fourth:
                    print(f"{i}/{j} = {first}/{fourth}")
                    answer *= i / j
    print(answer)


solve()