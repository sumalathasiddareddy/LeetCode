class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        num = len(citations)
        citations.sort() #O(nlogn)
        
        for i,n in enumerate(citations):
            if n>=(num-i):
               return num-i
        return 0
        