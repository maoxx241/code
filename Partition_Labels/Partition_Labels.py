class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res=[]
        d={}
        for i,c in enumerate(S):
            d[c]=i
        
        r =0
        l=0
        for i,c in enumerate(S):
            r= max(r,d[c])
            if i ==r:
                res.append(r-l+1)
                l=r+1
            
        return res