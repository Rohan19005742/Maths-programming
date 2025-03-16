import math

def getInput():
    with open("/Users/rohandesai/Documents/Learning/Maths-programming/Project-Euler/input_files/words.txt", "r") as file:
        for line in file:
            words = line.strip().split(",")  # Splitting by comma
    return words

alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

def getWordValue(word):
    total = 0
    for char in word:
        if char in alphabet:
            total+=1+alphabet.index(char)
    return total

def isTriangleNumber(num):
    a = 0.5
    b = 0.5
    c = -num
    x = (-b + math.sqrt(b*b - 4*a*c)) / (2*a)
    if 0.5 * int(x) * (int(x)+1) == num:
        return True
    else:
        return False

def solve():
    inputs = getInput()
    answer = 0
    for input in inputs:
        value = getWordValue(input)
        if isTriangleNumber(value):
            answer+=1
    return answer 

print(solve())


