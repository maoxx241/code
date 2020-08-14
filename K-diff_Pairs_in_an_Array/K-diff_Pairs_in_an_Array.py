class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count=collections.Counter(nums)
        dic={}
        if k<0:
            return 0
        if k==0:
            for i in count:
                if count[i]>1:
                    dic[i]=i
            return len(dic)
        for i in nums:
            if i+k in count:
                dic[i]=i+k
            elif i-k in count:
                dic[i-k]=i
        return len(dic)