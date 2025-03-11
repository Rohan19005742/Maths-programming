def fifth_power_sum(num):
    answer = 0
    num = str(num)
    for n in num:
        answer+=pow(int(n),5)
    return answer

def solve():
    answer = 0
    for x in range(10,1000000):
        if fifth_power_sum(x) == x:
            answer+=x
    print(answer)



solve()