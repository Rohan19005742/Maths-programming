def fibonacci(max_num):
    answer = 2
    prev_prev = 1
    prev = 2
    while prev < max_num:
        sum_ = prev_prev+prev
        prev_prev = prev
        prev = sum_
        if sum_ % 2 == 0 and sum_ < max_num:
            answer+=sum_
    return answer

print(fibonacci(4000000))