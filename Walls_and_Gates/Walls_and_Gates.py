class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
#         if not rooms: return
#         m=len(rooms)
#         n=len(rooms[0])
#         def dfs(r,c,val):
#             if r<0 or r>=m or c <0 or c>=n or rooms[r][c]==-1:
#                 return 
            
#             rooms[r][c]=min(rooms[r][c],val)
#             if rooms[r][c]!=val:
#                 return
            
#             dfs(r-1,c,val+1)
#             dfs(r+1,c,val+1)
#             dfs(r,c-1,val+1)
#             dfs(r,c+1,val+1)
            
        
#         for i in range(m):
#             for j in range(n):
#                 if rooms[i][j]==0:
#                     dfs(i,j,0)
                
        if not rooms:
            return []
		# Initialize the queue with all 0s
        R, C = len(rooms), len(rooms[0])
        q = collections.deque()
        for r in range(R):
            for c in range(C):
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= r+x < R and 0 <= c+y < C and rooms[r+x][c+y] > rooms[r][c]:
                    rooms[r+x][c+y] = rooms[r][c] + 1
                    q.append((r+x, c+y))