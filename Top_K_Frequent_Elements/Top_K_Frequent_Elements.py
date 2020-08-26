class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=collections.Counter(nums)
        ans=[]
        lst=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        for i in lst:
            ans.append(i[0])
            if len(ans)==k:
                return ans
    