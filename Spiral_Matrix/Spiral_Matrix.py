class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m=len(matrix)
        n=len(matrix[0])
        cur=0
        dir=0
        x,y=0,0
        res=[]
        for i in range(m*n):
            if dir==0:
                res.append(matrix[y][x])
                x+=1
                if x>=n-cur:
                    dir=1
                    x-=1
                    y+=1
            elif dir==1:
                res.append(matrix[y][x])
                y+=1
                if y>=m-cur:
                    y-=1
                    x-=1
                    dir=2
            elif dir==2:
                res.append(matrix[y][x])
                x-=1
                if x<0+cur:
                    x+=1
                    y-=1
                    dir=3
            elif dir==3:
                res.append(matrix[y][x])
                y-=1
                if y<0+cur+1:
                    cur+=1
                    x+=1
                    y+=1
                    dir=0
        
        return res