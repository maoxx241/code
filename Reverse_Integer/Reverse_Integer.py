class Solution:
    def reverse(self, x: int) -> int:
        # 1 or -1, (1,-1)[true or false]-> (false, true)
        sign = lambda x: x and (1, -1)[x < 0]
        # [::-1] reverse
        r = int(str(sign(x)*x)[::-1])
        #add -
        return (sign(x)*r, 0)[r > 2**31 - 1]
        