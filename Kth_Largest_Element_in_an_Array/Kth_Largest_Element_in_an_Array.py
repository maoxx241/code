class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        dic=collections.Counter(nums)
        for i in sorted(dic,reverse=True):
            k-=dic[i]
            if k<=0:
                return i
            