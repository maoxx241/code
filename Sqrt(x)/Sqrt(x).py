class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left=0
        right=x//2
        while left<=right:
            mid = left +(right -left)//2
            s=mid*mid
            if s==x:
                return mid
            elif s>x:
                right=mid-1
            elif s<x:
                left=mid+1
            
            
        return right