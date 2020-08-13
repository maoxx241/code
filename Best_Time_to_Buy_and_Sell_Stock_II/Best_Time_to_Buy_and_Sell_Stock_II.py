class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur=prices[0]
        res=0
        for i in range(len(prices)-1):
            if cur<prices[i+1]:
                res+=prices[i+1]-cur
            
            cur=prices[i+1]

        
        return res