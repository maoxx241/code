class Solution:
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]
    # def searchRange(self, nums, target):
    #     if not nums:
    #         return [-1,-1]
    #     def search(lo, hi):
    #         if nums[lo] == target == nums[hi]:
    #             return [lo, hi]
    #         if nums[lo] <= target <= nums[hi]:
    #             mid = (lo + hi) // 2
    #             l, r = search(lo, mid), search(mid+1, hi)
    #             return max(l, r) if -1 in l+r else [l[0], r[1]]
    #         return [-1, -1]
    #     return search(0, len(nums)-1)