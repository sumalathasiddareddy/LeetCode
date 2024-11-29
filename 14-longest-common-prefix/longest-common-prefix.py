class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            '''My solution
            prefix=""
            end=False
            n1=len(strs)
            n2=len(strs[0])

            for j in range(n2):
                char= strs[0][j]
                for i in range(n1):
                    if j>=len(strs[i]) or strs[i][j] !=char:
                        return prefix
                prefix+=char
                
            return prefix
            '''

            prefix=""
            strs.sort()
            n = min(len(strs[0]),len(strs[-1]))            

            for i in range(n):
                if strs[0][i]!=strs[-1][i]:
                    return prefix
                prefix+=strs[0][i]
            
            return prefix