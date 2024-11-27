class Solution:
    def jump(self, nums: List[int]) -> int:
      
        count,jumps,currEnd,currFarthest = 0,0,0,0

        for i, n in enumerate(nums):
            currFarthest = max(currFarthest,i+n)
            if i==currEnd and i<len(nums)-1:
                jumps+=1
                currEnd=currFarthest
        return jumps
        