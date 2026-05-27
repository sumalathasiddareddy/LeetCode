class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = max_length = 0
        chars = set()

        for right in s:
            while right in chars:
                chars.remove(s[left])
                left+=1
            chars.add(right)
            max_length = max(len(chars), max_length)
        
        return max_length 










       