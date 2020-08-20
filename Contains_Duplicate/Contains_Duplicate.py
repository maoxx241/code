class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i,num in enumerate(nums):
            if num not in dic:
                dic[num]=i
            else:
                return True
        
        return False