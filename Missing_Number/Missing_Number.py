class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum=0
        for num in nums:
            total_sum+=num
        return (0+len(nums))*(len(nums)+1)//2-total_sum