def sum_of_multiple_of_3_or_5(num):
    answer = 0
    for x in range(num):
        if x % 3 == 0 or x % 5 == 0:
            answer += x
    return answer

print(sum_of_multiple_of_3_or_5(1000))
