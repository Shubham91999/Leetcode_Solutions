class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x[0])
        # print(intervals)
        maxEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < maxEnd:
                return False
            else:
                maxEnd = max(maxEnd, intervals[i][1])
        return True
        

