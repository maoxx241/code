class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        count = collections.Counter({0: 1})
        for x in nums:
            step = collections.Counter()
            for y in count:
                step[y + x] += count[y]
                step[y - x] += count[y]
            count = step
        return count[S]