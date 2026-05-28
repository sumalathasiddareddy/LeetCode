class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        max_length=0
        curr_length =1

        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]-1:
                curr_length+=1
            else:
                max_length= max(max_length,curr_length)
                curr_length =1
       
        return max(max_length,curr_length)