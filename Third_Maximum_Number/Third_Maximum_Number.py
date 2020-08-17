class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        dic=collections.Counter(nums)

        dic=sorted(dic.items(),key = lambda x:x[0],reverse=True)

        return dic[0][0] if len(dic)<3 else dic[2][0]