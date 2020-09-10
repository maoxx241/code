class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
        # res = 0
        # while H:
        #     t = heapq.heappop(H)
        #     if t[1]:
        #         heapq.heappush(H, (t[2], 0, res + t[3]))
        #     else:
        #         res = max(res, t[2])
        # return res
        
        jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        dp = [[0, 0]]
        for s, e, p in jobs:
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]