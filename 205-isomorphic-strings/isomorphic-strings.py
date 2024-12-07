class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        news=""
        d={}
        c1=Counter(s)
        c2=Counter(t)
        
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=t[i]
                news+=t[i]
            else:
                news+=d[s[i]]

        return t==news and (len(c1.keys()) == len(c2.keys()) and sorted(list(c1.values()))==sorted(list(c2.values())))

