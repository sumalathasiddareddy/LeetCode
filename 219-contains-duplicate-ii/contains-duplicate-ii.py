class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        d=defaultdict(list)
        n=len(nums)

        for i in range(n):
            d[nums[i]].append(i)

        for indices in d.values():
            diff=0
            for i in range(len(indices)-1):
                diff= abs(indices[i]-indices[i+1])
                if diff<=k:
                    return True

        return False

        