class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        if len(s)<2:
            return []
        i=0
        res=[]
        while i<len(s)-1:
            if s[i]==s[i+1]=="+":
                res.append(s[0:i]+"--"+s[i+2:])
            i+=1
        
        return res