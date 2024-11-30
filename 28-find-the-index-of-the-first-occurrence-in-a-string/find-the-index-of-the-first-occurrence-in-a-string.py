class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        #return haystack.find(needle)

        m = len(haystack)
        n = len(needle)

        if m<n:
            return -1
        
        for i in range(m):
            flag=True
            if needle[0]==haystack[i]:
                k=i+1
                for j in range(1,n):
                    if k>=m or needle[j]!=haystack[k]:
                        flag=False
                        break
                    k+=1
                if flag:
                    return i

        return -1




























        