class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n=len(s)
        substr=set()
        ind=0
        maxLength=0

        for i in range(n):
            if s[i] not in substr:
                substr.add(s[i])
            else:
                maxLength = max(maxLength,len(substr))
                while s[ind]!=s[i]:
                    substr.remove(s[ind])
                    ind+=1
                ind+=1
        return max(maxLength,len(substr))










       