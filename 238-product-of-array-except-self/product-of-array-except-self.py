class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        answer=[1]*n
        prefix=[1]*n
        suffix=[1]*n
      
        prefix[0]=1
        suffix[n-1]=1
        
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for j in range(n-2,-1,-1):
            suffix[j] = suffix[j+1]*nums[j+1]

        for k in range(n):
            answer[k] = prefix[k]*suffix[k]

        return answer



        
            
    