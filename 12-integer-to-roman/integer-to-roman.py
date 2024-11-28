class Solution:
    def intToRoman(self, num: int) -> str:
        d={
        4:"IV",
        9:"IX" ,
        40:"XL",
        90:"XC",
        400:"CD", 
        900:"CM",
        1:"I",
        5:"V",
        10:"X",
        50:"L",
        100:"C",
        500:"D",
        1000:"M"
        }

        romanStr=""
        placeValue=1

        while num >0:
            n = (num%10) * placeValue
            num = num//10
            temp=""
            if n in d:
                romanStr = d[n] + romanStr
            else:
                if placeValue == 1:
                    if n>5:
                        temp += "V"
                        n=n-5
                    while n>0:
                        temp+="I"
                        n-=1
                elif placeValue == 10:
                    if n>50:
                        temp += "L"
                        n=n-50
                    while n>0:
                        temp+="X"
                        n-=10
                elif placeValue == 100:
                    if n>=500:
                        temp += "D"
                        n-=500
                    while n>0:
                        temp+="C"
                        n-=100
                elif placeValue == 1000:
                    while n>0:
                        temp += "M"
                        n-=1000
                        
                romanStr = temp + romanStr
            placeValue *=10                
            
        return romanStr