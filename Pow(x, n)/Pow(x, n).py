class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n<0: x=1/x
        # ans=1
        # for _ in range(abs(n)):
        #     ans*=x
        # return ans
        if n<0: x=1/x
        ans=1
        cur=x
        i=abs(n)
        while i:
            if i%2:
                ans*=cur
            cur*=cur
            i//=2
        return ans