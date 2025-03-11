def fibonacci():
    count = 2
    num1 = 1
    num2 = 1

    while len(str(num2)) != 1000:
        num3 = num1+num2
        num1 = num2
        num2 = num3
        count+=1
    print(count)

fibonacci()