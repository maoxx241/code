class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # dic=collections.Counter(nums1)-(collections.Counter(nums1)-collections.Counter(nums2))
        # res=[]
        # for i in dic:
        #     res+=(dic[i]*[i])
        # return res
        a, b = map(collections.Counter, (nums1, nums2))
        return list((a & b).elements())