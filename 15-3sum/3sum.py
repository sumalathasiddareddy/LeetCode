class Solution:
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res=set()
        n=len(nums)
        for i in range(n):
            target=-1*nums[i]
            j=i+1
            k=n-1
            while j<k:
                if nums[j]+nums[k] < target:
                    j+=1
                elif nums[j]+nums[k] > target:
                    k-=1
                else:
                    res.add(tuple(sorted([nums[i],nums[j],nums[k]])))
                    j+=1
                    k-=1

        return [list(tp) for tp in res]
        

            


            
                
            