class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans=0
        while num>0:
            if not num%2:
                num=num//2
            else:
                num-=1
            ans+=1
        return ans