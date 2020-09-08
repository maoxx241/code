class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dic=set()
        ans=[]
        for num in nums:
            if num not in dic:
                dic.add(num)
            else:
                ans.append(num)
        return ans
#         ans=[]
#         for num in nums:
#             if nums[abs(num)-1]<0:
#                 ans.append(abs(num))
#             nums[abs(num)-1]*=-1
        
#         return ans