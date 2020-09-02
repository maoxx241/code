class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic=collections.Counter(text)
        dic["l"]//=2
        dic["o"]//=2
        ans=float('inf')
        for c in "balon":
            ans=min(dic[c],ans)
        return ans