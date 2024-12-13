class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        
        start,i,maxCount=0,0,0
        nums= list(set(nums))
        nums.sort()
        n=len(nums)

        while i<n:            
            while i<n and nums[i]-nums[start] == (i-start):
                i+=1
            maxCount = max(maxCount,i-start)
            start=i
            i+=1
        
        return maxCount
       