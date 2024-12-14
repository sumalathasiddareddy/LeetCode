class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        n=len(nums)
        i,start=0,0
        res=[]

        while i<n:
            while i<n-1 and nums[i+1]-nums[i] == 1:
                i+=1
            if start==i:
                res.append(str(nums[i]))
                if i==n-1:
                    break            
            else:
                res.append(str(nums[start])+"->"+str(nums[i]))
            i+=1
            start=i

        return res
            


        