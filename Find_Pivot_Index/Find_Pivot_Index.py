class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
#         if not nums:
#             return -1
#         dic={0:0}
#         for i,num in enumerate(nums):
#             dic[i+1]=dic[i]+num
        
#         for index in dic:
#             if index+1 >len(nums):
#                 return -1
#             if dic[index]==dic[len(nums)]-dic[index+1]:
#                 return index
        
#         return -1
        
        S = sum(nums)
        leftsum = 0
        for i, x in enumerate(nums):
            if leftsum == (S - leftsum - x):
                return i
            leftsum += x
        return -1