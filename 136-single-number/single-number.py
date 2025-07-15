class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        nums.sort() #O(nlogn)
        n=len(nums)
        for i in range(n):#O(n)
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
        '''

        c = Counter(nums)
        for key,val in c.items():
            if val==1:
                return key
        return -1