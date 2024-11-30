class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        #news=''.join([char.lower() for char in s if char.isalnum()])
        #return news==news[::-1]

        chars = [char.lower() for char in s if char.isalnum()]
        for i in range(len(chars)//2):
            if chars[i]!=chars[~i]:
                return False
        return True

       