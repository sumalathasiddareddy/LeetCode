class Solution:
    def reverseWords(self, s: str) -> str:
        
        stack = []
        words = []
        s = s.strip()

        for char in s:
            if char != " ":
                stack.append(char)
            else:
                words.append("".join(stack))
                while stack:
                    stack.pop()

        if stack:
            words.append("".join(stack))
        return " ".join([word for word in words[::-1] if word])







        