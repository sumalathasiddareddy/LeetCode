class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        di = {}
        ind=0
        n=len(nums)

        for i in range(n):
            if nums[i] not in di or di[nums[i]]<2:
                nums[ind]=nums[i]
                ind+=1
                di[nums[i]] = di.get(nums[i],0)+1

        return ind


        