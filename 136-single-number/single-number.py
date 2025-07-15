class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        for i in range(n):
            if n==1:
                return nums[i]
            if i==0 and i<n-1:
                if nums[i]!=nums[i+1]:
                    return nums[i]
            if i==n-1:
                if nums[i]!=nums[i-1]:
                    return nums[i]
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
            
        return -1