class Solution:
    def isHappy(self, n: int) -> bool:

        num = []
        temp = 0
        Sum = 0

        while True:
            prevSum = Sum
            Sum = 0
            while n > 0:
                temp = n % 10
                Sum += temp * temp
                n = n // 10
            if Sum == 1:
                return True
            if Sum in num:
                return False
            num.append(Sum)
            n = Sum
