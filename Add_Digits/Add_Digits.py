class Solution:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        return num%9 if num %9 else 9