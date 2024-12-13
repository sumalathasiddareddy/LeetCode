class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        d=defaultdict(list)
        n=len(nums)

        for i in range(n):
            if nums[i] in d:
                if abs(d[nums[i]][-1] - i)<=k:
                   return True
            d[nums[i]].append(i)
        return False

        