class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        m,n = len(s),len(t)
        if m > n:
            return False
        ind=0
        for i in range(m):
            j=ind
            while j<n:
                if s[i] == t[j]:
                    ind=j+1
                    break
                j+=1
            else:
                return False
        return True
