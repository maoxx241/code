class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s :
            return True
        i=0
        limit=len(s)
        for c in t:
            if c==s[i]:
                i+=1
            if i==limit:
                return True
        
        return False