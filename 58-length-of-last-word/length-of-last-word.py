class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        #return len(s.strip().split(" ")[-1])

        s=s.strip()
        i =len(s)-1
        while i>=0 and s[i]!=" ":
            i-=1
        
        return len(s)-i-1 if i>=0 else len(s)
        