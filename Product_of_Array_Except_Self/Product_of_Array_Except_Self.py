class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        count=0
        s=1
        for i in nums:
            if i ==0:
                count+=1
                continue
            s*=i
        if count>1:
            return [0 for _ in range(len(nums))]

        
        if count==0:
            ans=[s for _ in range(len(nums))]
            for i in range(len(nums)):
                ans[i]//=nums[i]
        else:
            ans=[0 for _ in range(len(nums))]
            for i in range(len(nums)):
                if nums[i]==0:
                    ans[i]=s
                    continue
                ans[i]=0
        return ans