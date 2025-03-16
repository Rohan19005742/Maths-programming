import math
def self_powers(num):
    answer = 0
    for x in range(1,num+1):
        count = x
        for y in range(x-1):
            count *= x
        answer+=count
        if len(str(answer)) > 10:
            answer = int(str(answer)[len(str(answer))-10:len(str(answer))])
    print(answer)
self_powers(1000)