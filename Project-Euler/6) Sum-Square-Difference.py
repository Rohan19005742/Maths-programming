def sum_of_squares(num):
    answer = 1
    for x in range(2,num+1):
        answer += x*x
    return answer

def square_of_sum(num):
    answer = 1
    for x in range(2,num+1):
        answer += x
    return answer * answer

print(square_of_sum(100) - sum_of_squares(100))