class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        d={}
        i=0
        words = s.strip().split(" ")

        if len(words)!=len(pattern):
            return False

        for char in pattern:
            if (char in d and d[char]!=words[i]) or (char not in d and words[i] in d.values()):
                return False
            else:
                d[char]=words[i]
                i+=1

        return True


        