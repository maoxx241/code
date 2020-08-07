class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        cur=prices[0]
        ans=0
        for p in prices:
            if p < cur:
                cur=p
            ans=max(ans,p-cur)
        return ans