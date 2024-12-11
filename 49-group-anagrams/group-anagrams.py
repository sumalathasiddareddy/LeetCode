class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
       d=defaultdict(list)
       n=len(strs)
       
       for i in range(n):
            s=str(sorted(strs[i]))
            d[s].append(strs[i])
       return list(d.values())
        