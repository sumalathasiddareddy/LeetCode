class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        unique = set()
        ind =0

        for i in range(len(nums)):
            if nums[i] not in unique:
                nums[ind] = nums[i]
                unique.add(nums[i])
                ind+=1
        return ind


       