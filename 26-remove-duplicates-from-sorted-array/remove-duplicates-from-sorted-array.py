class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        uniqueEls=set()
        ind=0
        n=len(nums)

        for i in range(n):
            if nums[i] not in uniqueEls:
                nums[ind]=nums[i]
                ind+=1
                uniqueEls.add(nums[i])
        
        return ind