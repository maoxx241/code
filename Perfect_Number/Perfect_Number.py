class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # if num <= 0: return False
        # ans, SQRT = 0, int(num ** 0.5)
        # ans = sum(i + num//i for i in range(1, SQRT+1) if not num % i)
        # if num == SQRT ** 2: ans -= SQRT
        # return ans - num == num
    
        return num in set([6, 28, 496, 8128, 33550336, 8589869056])