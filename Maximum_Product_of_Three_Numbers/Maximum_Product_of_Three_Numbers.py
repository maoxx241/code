class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        return max(nums) * max(a * b for a, b in [heapq.nsmallest(2, nums), heapq.nlargest(3, nums)[1:]])