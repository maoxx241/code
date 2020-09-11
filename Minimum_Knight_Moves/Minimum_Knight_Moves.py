from collections import deque
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves=[(1,2),(2,1),(1,-2),(-1,2),(-1,-2),(-2,1),(2,-1),(-2,-1)]
#         visit=set()
        
#         queue=deque([(0,0,0)])
#         while queue:
#             i,j,step=queue.popleft()
#             if i==x and j==y:
#                 return step
            
#             for di,dj in moves:
#                 if (i+di,j+dj) not in visit:
#                     queue.append((i+di,j+dj,step+1))
#                     visit.add((i+di,j+dj))
        
        x, y = abs(x), abs(y)
        res = 0
        while x > 4 or y > 4:
            res += 1
            if x >= y:
                x -= 2
                y -= 1 if y >= 1 else -1
            else:
                x -= 1 if x >= 1 else -1
                y -= 2 
        
        # bfs        
        moves = ((2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1))
        queue = collections.deque([(0, 0, 0)])
        while queue:
            i, j, steps = queue.popleft()
            if i == x and j == y:
                return res + steps
            for di, dj in moves:
                if (x - i) * di > 0 or (y - j) * dj > 0: # move towards (x, y) at least in one direction
                    queue.append((i + di, j + dj, steps + 1))
            