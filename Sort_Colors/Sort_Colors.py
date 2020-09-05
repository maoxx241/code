class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
#         count=[0,0,0]
#         for num in nums:
#             count[num]+=1

#         count[1]+=count[0]
#         count[2]+=count[1]
        
#         for i in range(len(nums)):
#             if i <count[0]:
#                 nums[i]=0
#             elif i <count[1]:
#                 nums[i]=1
#             else:
#                 nums[i]=2
        
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
            