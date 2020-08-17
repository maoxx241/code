class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals=sorted(intervals,key = lambda x: x[0])
        time=intervals[0][0]
        for i in intervals:
            if i[0]<time:
                return False
            time=i[1]
        return True