class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

            prefix=""
            end=False

            for j in range(len(strs[0])):
                char= strs[0][j]
                for i in range(len(strs)):
                    if j>=len(strs[i]) or strs[i][j] !=char:
                        end=True
                        break
                if not end:
                    prefix+=char
                else:
                    break
            
            return prefix