class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=collections.Counter(nums)
        dic=sorted(dic.items(),key = lambda x: x[1],reverse=True)
        return dic[0][0]