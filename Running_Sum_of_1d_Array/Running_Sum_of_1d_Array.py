class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=[0]
        for num in nums:
            s.append(s[-1]+num)
        
        return s[1:]
            