def getInput():
    with open("/Users/rohandesai/Documents/Learning/Maths-programming/Project-Euler/input_files/names.txt", "r") as file:
        for line in file:
            words = line.strip().split(",")  # Splitting by comma
    return words

def solve():
    dic = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    inputs = getInput()
    inputs.sort()
    count = 0
    answer = 0
    for name in inputs:
        count+=1
        value = 0
        for x in range(1,len(name)-1):
            value+=dic[name[x]]
        answer+=value*count
    print(answer)

solve()