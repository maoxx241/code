class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ans=1
        prev=nums[0]
        c=1
        for n in nums:
            if n > prev:
                c+=1
            else:
                c=1
            ans=max(ans,c)
            prev=n
        return ans