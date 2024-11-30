class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        #news=''.join([char.lower() for char in s if char.isalnum()])
        #return news==news[::-1]

        s = [c.lower() for c in s if c.isalnum()]
        return all (s[i] == s[~i] for i in range(len(s)//2))


       