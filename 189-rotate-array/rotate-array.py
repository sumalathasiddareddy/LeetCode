class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        for i in range(k):#O(k)
            m=nums[-1]
            nums.pop()  #O(1)
            nums.insert(0,m) #O(n)
        
        #Overall: O(n*k)
        
        return
