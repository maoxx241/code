class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans=float('inf')
        left=0
        su=0
        for i in range(len(nums)):
            su+=nums[i]
            while su>=s:
                ans=min(ans,i-left+1)
                
                su-=nums[left]
                left+=1
        
        return ans if ans !=float('inf') else 0