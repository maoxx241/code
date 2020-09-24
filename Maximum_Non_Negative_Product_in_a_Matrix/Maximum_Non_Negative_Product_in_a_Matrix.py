class Solution:
#     def dfs(self,grid,row,col,current):
#         if (row,col,current) in self.memo:
#             return
#         if row==len(grid)-1 and col==len(grid[0])-1:
#             self.ans=max(self.ans,current)
#             return
        
#         self.memo.add((row,col,current))
#         if row+1<len(grid):
#             self.dfs(grid,row+1,col,current*grid[row+1][col])
#         if col+1<len(grid[0]):
#             self.dfs(grid,row,col+1,current*grid[row][col+1])
            
    
#     def maxProductPath(self, grid: List[List[int]]) -> int:
        
#         self.ans=-1
#         self.memo=set()
#         self.dfs(grid,0,0,grid[0][0])
#         if self.ans!=-1:
#             return self.ans % ((10**9)+7)
#         else:
#             return -1
    def maxProductPath(self, grid: List[List[int]]) -> int:
    #     rows, cols = len(grid), len(grid[0])
    #     dp = [(1, 1)] * cols
    #     for r, col in enumerate(grid):
    #         for c, item in enumerate(col):
    #             if r == 0 and c == 0:
    #                 dp[c] = (item, item)
    #             elif r == 0:
    #                 dp[c] = (item * dp[c-1][0], item * dp[c-1][1])
    #             elif c == 0:
    #                 dp[c] = (item * dp[c][0], item * dp[c][1])
    #             else:
    #                 m = min(map(lambda num: item * num, (*dp[c], *dp[c-1])))
    #                 M = max(map(lambda num: item * num, (*dp[c], *dp[c-1])))
    #                 dp[c] = (m, M)
    #     return dp[-1][1] % (10**9 + 7) if dp[-1][1] >= 0 else -1
        m, n = len(grid), len(grid[0])
        Max = [[0] * n for _ in range(m)]
        Min = [[0] * n for _ in range(m)]
        Max[0][0] = grid[0][0]
        Min[0][0] = grid[0][0]
        for j in range(1, n):
            Max[0][j] = Max[0][j - 1] * grid[0][j]
            Min[0][j] = Min[0][j - 1] * grid[0][j]

        for i in range(1, m):
            Max[i][0] = Max[i - 1][0] * grid[i][0]
            Min[i][0] = Min[i - 1][0] * grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] > 0:
                    Max[i][j] = max(Max[i - 1][j], Max[i][j - 1]) * grid[i][j]
                    Min[i][j] = min(Min[i - 1][j], Min[i][j - 1]) * grid[i][j]
                else:
                    Max[i][j] = min(Min[i - 1][j], Min[i][j - 1]) * grid[i][j]
                    Min[i][j] = max(Max[i - 1][j], Max[i][j - 1]) * grid[i][j]
        return Max[-1][-1] % int(1e9 + 7) if Max[-1][-1] >= 0 else -1