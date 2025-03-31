def is_pandigital(num1,num2):
    num3 = num1*num2
    nums = [1,2,3,4,5,6,7,8,9]
    count = 9

    for x in range(len(str(num1))):
        count-=1
        if int(str(num1)[x]) in nums:
            nums.remove(int(str(num1)[x]))
    
    for y in range(len(str(num2))):
        count-=1
        if int(str(num2)[y]) in nums:
            nums.remove(int(str(num2)[y]))

    for z in range(len(str(num3))):
        count-=1
        if int(str(num3)[z]) in nums:
            nums.remove(int(str(num3)[z]))
    
    return len(nums) == 0 and count == 0


def solve():
    answer = 0
    nums = {}
    for num1 in range(1,100):
        for num2 in range(1,2000):
            if is_pandigital(num1,num2):
                if num1*num2 not in nums:
                    answer+=num1*num2
                    nums[num1*num2] = 0
                
    print(answer)
solve()

    