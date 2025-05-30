class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c1 = Counter(nums)
        freq = [[] for i in range((len(nums)+1))]

        for key in c1.keys():
            freq[c1[key]].append(key)

        res=[]

        for i in range(len(nums),-1,-1):
            if freq[i]:
                for j in freq[i]:
                    res.append(j)
                if len(res)==k:
                    return res
            
        return []