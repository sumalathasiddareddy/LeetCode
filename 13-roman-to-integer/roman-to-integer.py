class Solution:
    def romanToInt(self, s: str) -> int:

        d = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num=0
        n=len(s)

        for i in range(n):
            num += d[s[i]]
            if i>0 and s[i] in ("V","X"):
                if s[i-1] == "I":
                    num = num-2
            elif i>0 and s[i] in ("L","C"):
                if s[i-1] == "X":
                    num = num-20
            elif i>0 and s[i] in ("D","M"):
                if s[i-1] == "C":
                    num = num-200
           
        return num




        