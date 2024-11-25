class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        di = {}
        ind=0
        n=len(nums)

        for i in range(n):
            k=nums[i]
            if k not in di or di[k]<2:
                nums[ind]=k
                ind+=1
                di[k] = di.get(k,0)+1

        return ind


        