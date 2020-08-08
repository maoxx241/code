class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d={}
        for point in points:
            d[(point[0],point[1])]=point[0]*point[0]+point[1]*point[1]
        d=sorted(d.items(), key=lambda t: t[1])
        res=[]
        for i in range(K):
            res.append([d[i][0][0],d[i][0][1]])
        return res