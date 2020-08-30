class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]
        print(nums)
        longest = max([len(x) for x in nums], default=0)
        print(longest)
        nums.sort(key=lambda x: x*(longest//len(x)+1), reverse=True)
        if nums and nums[0] == '0':
            return '0'
        return ''.join(nums)