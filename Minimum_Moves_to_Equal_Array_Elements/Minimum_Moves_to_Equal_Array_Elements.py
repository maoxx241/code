class Solution:
    def minMoves(self, nums: List[int]) -> int:
        l=len(nums)
        s=sum(nums)
        mn=min(nums)
        return s-l*mn