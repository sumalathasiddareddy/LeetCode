class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        answer=[1]*n
        prefix=[1]*n
             
        prefix[0]=1
               
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        temp=1
        for j in range(n-1,-1,-1):
            answer[j] = prefix[j]*temp
            temp*=nums[j]

        return answer


        
            
    