class Solution:
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res=[]
        n=len(nums)

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=-1*nums[i]
            j=i+1
            k=n-1
            while j<k:
                if nums[j]+nums[k] < target:
                    j+=1
                elif nums[j]+nums[k] > target:
                    k-=1
                else:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                    k-=1
                    while nums[k]==nums[k+1] and k>j:
                        k-=1
        return res
        

            


            
                
            