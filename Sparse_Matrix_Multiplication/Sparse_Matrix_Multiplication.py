class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        if not A or not A[0] or not B or not B[0]:
            return [[]]
        sparse_A = self.get_none_zero(A)
        sparse_B = self.get_none_zero(B)
        n, m, k = len(A), len(A[0]), len(B[0])
        C = [[0] * k for _ in range(n)]
        for i, j, val_A in sparse_A:
            for x, y, val_B in sparse_B:
                if j == x:
                    C[i][y] += val_A * val_B
        return C

    def get_none_zero(self, A):
        res = []
        n, m = len(A), len(A[0])
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    continue
                res.append((i, j, A[i][j]))
        return res