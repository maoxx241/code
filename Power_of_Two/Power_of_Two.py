class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n<0:
        #     return False
        # s=bin(n)
        # return collections.Counter(s[2:])['1']==1
        if n == 0:
            return False
        return n & (n - 1) == 0