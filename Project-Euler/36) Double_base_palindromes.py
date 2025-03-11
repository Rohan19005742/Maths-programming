def is_Palindrome(num):
    lis = list(str(num))
    reverse = list(str(num))
    reverse.reverse()
    if lis == reverse:
        return True
    return False

def solve():
    answer = 0
    for x in range(1,1000000):
        if is_Palindrome(x) and is_Palindrome(bin(x)[2:]):
            answer+=x
    print(answer)


solve()