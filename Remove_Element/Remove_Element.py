class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0

        i = 0
        length = len(nums)
        for j in range(0, length):
            if nums[j] != val:
                nums[i] = nums[j]
                i = i+1
        return i