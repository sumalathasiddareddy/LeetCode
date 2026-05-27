class Solution:
    def longestPalindrome(self, s: str) -> str:
       substr =[]
       max_length=0
       
       if s== s[0]*len(s):
                return s
       
       for i in range(len(s)-1):
            l=i
            for r in range(l+2,len(s)+1):   
                    if s[l:r] == s[l:r][::-1]:
                        if max_length < len(s[l:r]):
                            max_length = len(s[l:r])
                            substr = s[l:r]
        
       if max_length>0 :
        return substr
       else:
        return s[0]
    
     

    

        