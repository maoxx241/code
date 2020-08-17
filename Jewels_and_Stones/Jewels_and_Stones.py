class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        dic=collections.Counter(J)
        ans=0
        for c in S:
            if c in dic:
                ans+=1
        return ans