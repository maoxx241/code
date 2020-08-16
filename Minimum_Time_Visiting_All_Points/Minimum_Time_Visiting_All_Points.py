class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans =0
        for i in range(1,len(points)):
            prev=points[i-1]
            cur=points[i]
            ans+=max(abs(prev[0]-cur[0]),abs(prev[1]-cur[1]))
        
        return ans