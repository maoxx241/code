class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(word, i, j, match_idx, directions, board, visited):
            if match_idx == len(word) - 1:
                return True
            # try all four directions
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                # if within the board, never visited, and matches the current char, keep matching the next char
                if 0 <= x < len(board) and 0 <= y < len(board[0]) and visited[x][y] == False and board[x][y] == word[match_idx + 1]:
                    visited[x][y] = True
                    if dfs(word, x, y, match_idx + 1, directions, board, visited):
                        return True
                    visited[x][y] = False
        
        m = len(board)
        n = len(board[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        visited = [[False for _ in range(n)] for _ in range(m)]
        # find the starting char
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    match_idx = 0
                    if dfs(word, i, j, match_idx, directions, board, visited):
                        return True
                    visited[i][j] = False
        return False