class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
       d={}
       n=len(strs)

       for i in range(n):
            s=str(sorted(strs[i]))
            if s in d:
                d[s].append(strs[i])
            else:
                d[s] = [strs[i]]

        
       return list(d.values())
        