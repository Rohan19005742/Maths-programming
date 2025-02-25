def is_Palindrome(num):
    lis = list(str(num))
    reverse = list(str(num))
    reverse.reverse()
    if lis == reverse:
        return True
    return False

def largest_palindrome_from_product(num):
    palindromes = []
    for x in range(num,-1,-1):
        for y in range(num,-1,-1):
            if is_Palindrome(x*y):
                palindromes.append(x*y)
    return max(palindromes)
            

    
print(largest_palindrome_from_product(999))