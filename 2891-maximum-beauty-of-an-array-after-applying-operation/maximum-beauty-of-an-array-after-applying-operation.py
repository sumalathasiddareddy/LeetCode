class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:

            nums.sort()
            n=len(nums)
            maxCount=1
            start=0

                      
            for i in range(1,n):
                while nums[i]-nums[start]>(k*2):
                    start+=1
                maxCount = max(i-start+1,maxCount)

            return maxCount
        