class Solution:
     def orangesRotting(self, grid: List[List[int]]) -> int:
        rst, xlen, ylen = 0, len(grid), len(grid[0])
        rot = {(i, j) for i in range(xlen) for j in range(ylen) if grid[i][j] == 2}
        fresh = sum(i == 1 for row in grid for i in row)
        while fresh:
            rot = {(x, y) for i, j in rot for x, y in 
                   [(i+1, j), (i-1, j), (i, j+1), (i, j-1)] 
                   if 0<=x<xlen and 0<=y<ylen and grid[x][y] == 1}
            if not rot: 
                return -1
            fresh, rst = fresh - len(rot), rst + 1
            for i, j in rot: 
                grid[i][j] = 2
        return rst