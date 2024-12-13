class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums=list(set(nums))
        nums.sort()
        n=len(nums)
        i=0
        maxCount=0

        if n==1:
            return 1
        if n==0:
            return 0

        while i<n-1:
            j=i
            while j<n-1 and nums[j+1]-nums[j] == 1:
                j+=1
            maxCount=max(maxCount,j-i+1)
            i=j+1

        return maxCount
        