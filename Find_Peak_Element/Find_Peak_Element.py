class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        
        while left <right:
            mid1 = (left+right)//2
            mid2 =mid1+1
            if nums[mid1]<nums[mid2]:
                left=mid2
            else:
                right=mid1
        
        return left