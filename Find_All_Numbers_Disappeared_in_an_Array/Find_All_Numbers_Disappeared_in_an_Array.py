class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dic=collections.Counter(nums)
        res=[]
        for i in range(1,len(nums)+1):
            if i not in dic:
                res.append(i)
        
        return res