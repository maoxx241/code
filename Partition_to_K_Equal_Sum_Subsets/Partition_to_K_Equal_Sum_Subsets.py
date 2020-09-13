class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if k <= 0 or total % k != 0 or len(nums) == 0 or k > len(nums):
            return False

        nums.sort(reverse=True)
        targets = [total // k] * k

        if nums[0] > targets[0]:
            return False

        def dfs(i):
            if i == len(nums):
                return True
            visited = set()
            for j in range(k):
                if targets[j] >= nums[i] and targets[j] not in visited:
                    visited.add(targets[j])
                    targets[j] -= nums[i]
                    if dfs(i + 1):
                        return True
                    targets[j] += nums[i]
            return False

        return dfs(0)