class Solution:
    def reverseWords(self, s: str) -> str:
        #solution using split()
        '''
        words = s.strip().split(" ")
        return " ".join([word for word in words[::-1] if word])
        '''

        #solution without split()
        s=s.strip()
        stack=[]
        word=''
        i=0

        while i<len(s):
            if s[i]!=" ":
                while i<len(s) and s[i]!=" ":
                    word+=s[i]
                    i+=1
                stack.append(word)
                word=""
            i+=1
        s=""
        while stack:
            s += stack.pop() + " "
        
        return s.strip()








        