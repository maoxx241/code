class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # if len(nums)==1:
        #     return 1
        dic=set(nums)

        ans=0
        for num in dic:
            if num - 1 not in dic:
                current_num = num
                current_streak = 1

                while current_num + 1 in dic:
                    current_num += 1
                    current_streak += 1

                ans = max(ans, current_streak)

        return ans