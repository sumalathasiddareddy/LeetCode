class Solution:
    def canJump(self, nums: List[int]) -> bool:

        steps=0

        for n in nums:
            if steps<0:
                return False
            elif n > steps:
                steps = n
            steps-=1
        
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        ''' My solution
        def takeNSteps(currPos,steps,nums)->bool:
            prevPos=currPos
            currPos+=steps
            if currPos>=len(nums)-1:
                return True
            if currPos == prevPos:
                return False
            for j in range(nums[currPos],-1,-1):
                if takeNSteps(currPos,j,nums):
                    return True
            return False

        if takeNSteps(-1,1,nums):
            return True

        return False '''
       