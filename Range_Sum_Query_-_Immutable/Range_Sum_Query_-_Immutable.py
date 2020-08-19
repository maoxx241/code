class NumArray:

    def __init__(self, nums: List[int]):
        self.dic={-1:0}
        for i,num in enumerate(nums):
            self.dic[i]=self.dic[i-1]+num

    def sumRange(self, i: int, j: int) -> int:
        return self.dic[j]-self.dic[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)