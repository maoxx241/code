class Solution:
    def rob(self, nums: List[int]) -> int:
        preMax=0
        curMax=0
        for i in nums:
            temp=curMax
            curMax=max(preMax+i,curMax)
            preMax=temp
        
        return curMax
        
        