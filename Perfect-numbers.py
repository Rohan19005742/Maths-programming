'''
Description of problem: A number is perfect if all of its factors excuding the number it self, add up to the number.
e.g: 6, factors of 6 are 1,2 and 3, 1+2+3 = 6
We are yet to find an odd perfect number.

solution: for even perfect numbers, euler found a formula: (2^p - 1) * 2^(p-1)) 
where (2^p - 1) has to be a prime number
'''

class Solution:
    def checkPrime(self, num):
        for x in range(2,int(num/2)+1):
            if num % x == 0:
                return False
        return True
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        if num % 2 == 1:
            return False
        x = 0
        count = 1
        store = 0
        while x < num:
            x = (pow(2,count) - 1) * pow(2,count-1)
            store = (pow(2,count) - 1)
            count+=1
        if x == num:
            for x in range(2,int(store/2)):
                if store % x == 0:
                    return False
            return True
        return False