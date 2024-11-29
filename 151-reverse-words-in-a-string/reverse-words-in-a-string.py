class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.strip().split(" ")
        return " ".join([word for word in words[::-1] if word])



        