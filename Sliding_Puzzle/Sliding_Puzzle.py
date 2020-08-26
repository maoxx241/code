class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(d) for row in board for d in row)

        dq, seen = collections.deque(), {s}
        
        dq.append((s, s.index('0')))

        steps, height, width = 0, len(board), len(board[0]) 

        while dq:
            for _ in range(len(dq)):
                t, i= dq.popleft()

                if t == '123450':
                    return steps
                x, y = i // width, i % width
                for r, c in (x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y):
                    if height > r >= 0 <= c < width:
                        ch = [d for d in t]

                        ch[i], ch[r * width + c] = ch[r * width + c], '0' # swap '0' and its neighbor.
                        s = ''.join(ch)

                        if s not in seen:
                            seen.add(s)
                            dq.append((s, r * width + c))

            steps += 1              
        return -1