class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # 1. MinHeap
        # if not intervals:
        #     return 0

        # # Sort intervals by start time
        # intervals.sort(key=lambda x: x[0])

        # min_heap = []  # Min-heap to track end times of meetings

        # for interval in intervals:
        #     if min_heap and min_heap[0] <= interval[0]:  # Check if any room is free
        #         heapq.heappop(min_heap)  # Remove the room with the earliest end time

        #     heapq.heappush(min_heap, interval[1])  # Add the new meeting's end time

        # return len(min_heap)

        # 2. Two Pointers
        start = []
        end = []
        for s, e in intervals:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res