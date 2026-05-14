class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        n= min(len(strs[0]),len(strs[-1]))
        prefix=""

        for i in range(n):
            if strs[0][i]!=strs[-1][i]:
                return prefix
            else:
                prefix += strs[0][i]
        return prefix