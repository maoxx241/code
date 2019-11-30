class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
#         i=0
#         while i<len(nums)-1:
#             if nums[i]==nums[i+1]:
#                 nums.pop(i+1)
#                 i-=1
#             i+=1
        
#         return len(nums)
        if not nums:
            return 0

        i = 0
        length = len(nums)
        for j in range(1, length):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i = i+1
        return i+1