class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #nums.sort()
        #return nums[len(nums)//2]

        counter = Counter(nums)
        maxV=0
        for k,v in counter.items():
            if v>maxV:
                maxV = v
                key = k

        return key    

       
        