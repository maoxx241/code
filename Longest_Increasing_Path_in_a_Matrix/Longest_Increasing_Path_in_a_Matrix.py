class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        self.depth=1
        self.table = {}
        
        def dfs(x, y, prev):
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] <= prev: 
                return 0
        
            if (x,y) in self.table: 
                return self.table[(x,y)]
        
            depth = 1 + max(dfs(x+1, y, matrix[x][y]), dfs(x-1, y, matrix[x][y]), dfs(x, y+1, matrix[x][y]), dfs(x, y-1, matrix[x][y]))
        
            self.depth = max(self.depth, depth)
            self.table[(x,y)] = depth
            return depth
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, -1)
    
        return self.depth

        
        
        
