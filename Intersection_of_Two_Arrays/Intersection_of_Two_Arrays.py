class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1=collections.Counter(nums1)
        dic2=collections.Counter(nums2)
        res=[]
        for i in dic1:
            if i in dic2:
                res.append(i)
        
        return res