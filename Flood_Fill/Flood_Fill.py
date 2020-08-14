class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def BFS(i,j,key):
            if 0>i or i>=len(image) or 0>j or j>=len(image[0]) or image[i][j]!=key or image[i][j]==newColor:
                return
            
            image[i][j]=newColor
            BFS(i+1,j,key)
            BFS(i-1,j,key)
            BFS(i,j+1,key)
            BFS(i,j-1,key)
        
        k=image[sr][sc]
        BFS(sr,sc,k)
        return image