class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        s = sum(machines)
        
        if s%len(machines)!=0:
            return -1
        
        avg=s//len(machines)# int 
        count=0
        ans=0
        for i in machines:
            count+=i-avg
            ans=max(ans,max(abs(count),i-avg))
        return ans