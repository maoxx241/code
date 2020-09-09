class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if len(heightMap) == 0:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])
        heap = []
        vst = set()

        # init , put surrounding into heap
        for i in [0, m - 1]:
            for j in range(n):
                heap.append((heightMap[i][j], i, j))
                vst.add((i, j))

        for j in [0, n - 1]:
            for i in range(m):
                if (i, j) in vst:
                    continue

                heap.append((heightMap[i][j], i, j))
                vst.add((i, j))

        heapq.heapify(heap)

        dxy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        ans = 0
        mx = float('-inf')

        while heap:

            h, x, y = heapq.heappop(heap)
            mx = max(h, mx)

            for dx, dy in dxy:
                nx = x + dx
                ny = y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                if (nx, ny) in vst:
                    continue

                if mx > heightMap[nx][ny]:
                    ans += mx - heightMap[nx][ny]

                itm = (heightMap[nx][ny], nx, ny)
                heapq.heappush(heap, itm)
                vst.add((nx, ny))

        return ans