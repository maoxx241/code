class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        m=0
        s=0
        for n in nums:
            s+=n
            m=min(m,s)
        return 1-m